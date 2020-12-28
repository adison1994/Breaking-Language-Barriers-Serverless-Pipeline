import boto3
from botocore.config import Config
import logging
import time
import ast

region = 'us-east-1'
client = boto3.client('translate', region_name = region)
s3_client = boto3.client('s3', region_name = region)
bucket_1 = ''
bucket_2 = ''
bucket_3 = ''
bucket_4 = ''


def get_language_codes(language):

    language_map = {'Danish': 'da',
                    'Dutch': 'nl',
                    'French': 'fr',
                    'German': 'de',
                    'Italian': 'it',
                    'English': 'en',
                    'Spanish': 'es',
                    'Arabic': 'arb', 
                    'Chinese': 'zh',
                    'Hindi': 'hi', 
                    'Japanese': 'ja',
                    'Polish': 'pl',
                    'Russian': 'ru',
                    'Turkish': 'tr',
                    'Portuguese': 'pt'}

    lang_code = language_map[language]
    return lang_code



def language_translate(languages, accent_map, username, orignal_transcript_f):
	text_trans_map = {}
	s3_file_path = 'English/{}'.format(orignal_transcript_f)
	response = s3_client.get_object(Bucket=bucket_1, Key=s3_file_path)
	text = response['Body'].read().decode('utf-8')
	text= text[:4800]

	for language in languages:

		timestr = time.strftime("%Y%m%d-%H%M%S")
		trans_text_f_tmp = "/tmp/" + username + "_trans_text_" + timestr + '.txt'
		trans_text_f = username + "_trans_text_" + timestr + '.txt'
		
		#pick voice id & Gender from dynamo based on lang
		language_code = get_language_codes(language) 
		response = client.translate_text(
		    Text=text,
		    SourceLanguageCode='Auto',
		    TargetLanguageCode=language_code
			)

		with open(trans_text_f_tmp, 'w', encoding="utf-8") as trans_f:
			trans_f.write(response['TranslatedText'])
		trans_f.close()
		
		trans_text_path = language + '/{}'.format(trans_text_f)
		response = s3_client.upload_file(Filename=trans_text_f_tmp, Bucket=bucket_2, Key=trans_text_path)
		text_trans_map[language] = trans_text_f
	return text_trans_map


def language_translate_summary(languages, accent_map, username, summary_text_f):
	summary_text_trans_map = {}
	s3_file_path = 'English/{}'.format(summary_text_f)
	response = s3_client.get_object(Bucket=bucket_3, Key=s3_file_path)
	text = response['Body'].read().decode('utf-8')

	for language in languages:

		timestr = time.strftime("%Y%m%d-%H%M%S")
		trans_text_f_tmp = "/tmp/" + username + "_trans_text_" + timestr + '.txt'
		trans_text_f = username + "_trans_text_" + timestr + '.txt'
		
		#pick voice id & Gender from dynamo based on lang
		language_code = get_language_codes(language) 
		response = client.translate_text(
		    Text=text,
		    SourceLanguageCode='Auto',
		    TargetLanguageCode=language_code
			)

		with open(trans_text_f_tmp, 'w', encoding="utf-8") as trans_f:
			trans_f.write(response['TranslatedText'])
		trans_f.close()
		
		trans_text_path = language + '/{}'.format(trans_text_f)
		response = s3_client.upload_file(Filename=trans_text_f_tmp, Bucket=bucket_4, Key=trans_text_path)
		summary_text_trans_map[language] = trans_text_f
	return summary_text_trans_map


def lambda_handler(event, context):
	Summary_txt_trans_map = {}

	try:
		Summarize = event['body']['Summarize']
		Username = event['body']['Username']
		Langauges = ast.literal_eval(event['body']['Langauges'])
		User_selection_map = ast.literal_eval(event['body']['User_selection_map'])
		Podcast_map = ast.literal_eval(event['body']['Podcast_map'])
		TranslationorNER = event['body']['TranslationorNER']
		Transcribe_file = Podcast_map['Transcribe_file']
		Gender = User_selection_map['Gender']
		OutputAudio = User_selection_map['OutputAudio']

		Text_trans_map = language_translate(Langauges, Gender, Username, Transcribe_file)

		if Summarize == 'Summarize':
			Summary_text_f = Podcast_map['Summary_text_file']
			Summary_txt_trans_map = language_translate_summary(Langauges, Gender, Username, Summary_text_f)
		
		return {
            "body":{
                "Text_trans_map": str(Text_trans_map),
                "Summary_txt_trans_map": str(Summary_txt_trans_map),
                "TranslationorNER": str(TranslationorNER),
                "Podcast_map": str(Podcast_map),
	            "User_selection_map": str(User_selection_map), 
                "Langauges":str(Langauges),
                "Username": Username,
                "Transcribe_file": Transcribe_file, 
                "Summarize": Summarize,
                "OutputAudio": OutputAudio

            }
        }
	except Exception as e:
		logging.error('Exception: %s. Unable to Scrape Audio files' % e)
		raise e
