import boto3
from botocore.config import Config
import logging
import time
import ast

region = ''
polly_client = boto3.client('polly', config=Config(
region_name=region))
s3_client = boto3.client('s3', region_name = region)
bucket_1 = ''
bucket_2 = ''
bucket_3 = ''
bucket_4 = ''
bucket_5 = ''
bucket_6 = ''


lang_gender_map = {'Male': {'Danish': {'Code': 'da-DK','Voice': 'Mads'},
                            'Dutch': {'Code': 'nl-NL', 'Voice': 'Ruben'},
                            'French': {'Code': 'fr-FR', 'Voice': 'Mathieu'},
                            'German': {'Code': 'de-DE', 'Voice': 'Hans'},
                            'Italian': {'Code': 'it-IT', 'Voice': 'Giorgio'},
                            'English': {'Code': 'en-US', 'Voice': 'Matthew'},
                            'Spanish': {'Code': 'es-ES', 'Voice': 'Enrique'},
                           'Arabic': {'Code': 'arb', 'Voice': 'Zeina'}, 
                        	'Chinese': {'Code': 'cmn-CN', 'Voice': 'Zhiyu'},
                           'Hindi': {'Code': 'hi-IN', 'Voice': 'Aditi'},
                           'Japanese': {'Code': 'ja-JP', 'Voice': 'Takumi'},
                           'Polish': {'Code': 'pl-PL', 'Voice': 'Jacek'}, 
                        	'Russian': {'Code': 'ru-RU', 'Voice': 'Maxim'},
                           'Turkish': {'Code': 'tr-TR', 'Voice': 'Filiz'},
                           'Portuguese': {'Code': 'pt-PT', 'Voice': 'Ricardo'}}, 

                    'Female': {'Arabic': {'Code': 'arb', 'Voice': 'Zeina'}, 
                        'Chinese': {'Code': 'cmn-CN', 'Voice': 'Zhiyu'},
                        'Danish': {'Code': 'da-DK', 'Voice': 'Naja'},
                        'Dutch': {'Code': 'nl-NL', 'Voice': 'Lotte'},
                        'French': {'Code': 'fr-FR', 'Voice': 'Celine'},
                        'German': {'Code': 'de-DE', 'Voice': 'Marlene'},
                         'Hindi': {'Code': 'hi-IN', 'Voice': 'Aditi'},
                         'Italian': {'Code': 'it-IT', 'Voice': 'Bianca'}, 
                        'English': {'Code': 'en-US', 'Voice': 'Joanna'},
                        'Spanish': {'Code': 'es-ES', 'Voice': 'Lucia'},
                        'Japanese': {'Code': 'ja-JP', 'Voice': 'Mizuki'},
                           'Polish': {'Code': 'pl-PL', 'Voice': 'Ewa'}, 
                        	'Russian': {'Code': 'ru-RU', 'Voice': 'Tatyana'},
                           'Turkish': {'Code': 'tr-TR', 'Voice': 'Filiz'},
                           'Portuguese': {'Code': 'pt-PT', 'Voice': 'Camila'}}
}


def fetch_voice_id(language, gender):
	voice_id =  lang_gender_map[gender][language]['Voice']
	return voice_id


def text_to_Speech(text_trans_map, username, gender):
	audio_trans_map = {}
	for language in text_trans_map.keys():

		text_file_name = text_trans_map[language]
		s3_file_path= language + '/{}'.format(text_file_name)
		response = s3_client.get_object(Bucket=bucket_2, Key=s3_file_path)
		text = response['Body'].read().decode('utf-8')
		text = text[:2800]

		timestr = time.strftime("%Y%m%d-%H%M%S")
		polly_audio_f_tmp = "/tmp/" + username + "_polly_audio_" + timestr + '.mp3'
		polly_audio_f = username + "_polly_audio_" + timestr + '.mp3'
		
		voiceId = fetch_voice_id(language, gender)
		response = polly_client.synthesize_speech(Text=text, VoiceId=voiceId, OutputFormat='mp3')
		f = open(polly_audio_f_tmp, 'wb')
		f.write(response['AudioStream'].read())

		response['AudioStream'].close()
		f.close()
		audio_file_path = language + '/{}'.format(polly_audio_f)
		response = s3_client.upload_file(Filename=polly_audio_f_tmp, Bucket=bucket_1, Key=audio_file_path)
		audio_trans_map[language] = polly_audio_f
		# save file names in Db
	return audio_trans_map


def summary_text_to_Speech(text_trans_map, username, gender):
	audio_trans_map = {}
	for language in text_trans_map.keys():

		text_file_name = text_trans_map[language]
		s3_file_path= language + '/{}'.format(text_file_name)
		response = s3_client.get_object(Bucket=bucket_5, Key=s3_file_path)
		text = response['Body'].read().decode('utf-8')
		text = text[:2800]
		
		timestr = time.strftime("%Y%m%d-%H%M%S")
		polly_audio_f_tmp = "/tmp/" + username + "_polly_audio_" + timestr + '.mp3'
		polly_audio_f = username + "_polly_audio_" + timestr + '.mp3'
		
		voiceId = fetch_voice_id(language, gender)
		response = polly_client.synthesize_speech(Text=text, VoiceId=voiceId, OutputFormat='mp3')
		f = open(polly_audio_f_tmp, 'wb')
		f.write(response['AudioStream'].read())

		response['AudioStream'].close()
		f.close()
		audio_file_path = language + '/{}'.format(polly_audio_f)
		response = s3_client.upload_file(Filename=polly_audio_f_tmp, Bucket=bucket_6, Key=audio_file_path)
		audio_trans_map[language] = polly_audio_f
	return audio_trans_map

def text_to_Speech_Masking(ner_mask_file, username, gender):
	language = 'English'
	s3_file_path= 'SSML/{}'.format(ner_mask_file)
	response = s3_client.get_object(Bucket=bucket_4, Key=s3_file_path)
	text = response['Body'].read().decode('utf-8')
	text = text[:1200]
	text_ =  "'''" + text +  "</speak>"+ "'''"
	text_ = ast.literal_eval(text_)

	timestr = time.strftime("%Y%m%d-%H%M%S")
	polly_audio_f_tmp = "/tmp/" + username + "_polly_audio_" + timestr + '.mp3'
	polly_audio_f = username + "_polly_audio_" + timestr + '.mp3'
	voiceId = fetch_voice_id(language, gender)
	response = polly_client.synthesize_speech(Text=text_, VoiceId=voiceId, OutputFormat='mp3', TextType='ssml')
	f = open(polly_audio_f_tmp, 'wb')
	f.write(response['AudioStream'].read())

	response['AudioStream'].close()
	f.close()
	response = s3_client.upload_file(Filename=polly_audio_f_tmp, Bucket=bucket_3, Key='English/{}'.format(polly_audio_f)) 
	return polly_audio_f



def lambda_handler(event, context):
	
	audio_trans_map = {}
	audio_summ_trans_map = {}
	Summary_txt_trans_map = {}
	Text_trans_map = {}

	try:
		NER_Masking_map = {}
		Username = event['body']['Username']
		Langauges = ast.literal_eval(event['body']['Langauges'])
		User_selection_map = ast.literal_eval(event['body']['User_selection_map'])
		Podcast_map = ast.literal_eval(event['body']['Podcast_map'])
		Transcribe_file = Podcast_map['Transcribe_file']
		TranslationorNER = event['body']['TranslationorNER']
		Summary_option = User_selection_map['Summarize']
		Gender = User_selection_map['Gender']
		OutputAudio = event['body']['OutputAudio']
		Sf_Execution = Podcast_map['Sf_Execution']

		if TranslationorNER == 'NER':
			NER_Masking_map = ast.literal_eval(event['body']['NER_Masking_map'])
			ner_mask_file = NER_Masking_map['Masked_NER_file']
			audio_masked_file = text_to_Speech_Masking(ner_mask_file, Username,Gender)
			Podcast_map['Audio_masked_file'] = audio_masked_file
			NER_Masking_map['Audio_masked_file'] = audio_masked_file
		else:
			Text_trans_map = ast.literal_eval(event['body']['Text_trans_map'])
			audio_trans_map = text_to_Speech(Text_trans_map, Username, Gender)

			if Summary_option == 'Summarize':
				Summary_txt_trans_map = ast.literal_eval(event['body']['Summary_txt_trans_map'])	
				audio_summ_trans_map = summary_text_to_Speech(Summary_txt_trans_map, Username, Gender)

		return {
            "body":{
                "Text_trans_map": str(Text_trans_map),
                "Summary_txt_trans_map": str(Summary_txt_trans_map),
                "TranslationorNER": TranslationorNER,
                "Podcast_map": str(Podcast_map),
	            "User_selection_map": str(User_selection_map), 
                "Langauges":str(Langauges),
                "Username": Username,
                "Transcribe_file": Transcribe_file, 
                "Summarize": Summary_option,
                "Gender": Gender,
                "OutputAudio": OutputAudio,
                "Sf_Execution": Sf_Execution,
                "NER_Masking_map": str(NER_Masking_map),
                "Audio_trans_map": str(audio_trans_map),
                "audio_summ_trans_map":str(audio_summ_trans_map)

            }
        }
	except Exception as e:
		logging.error('Exception: %s. Unable to Scrape Audio files' % e)
		raise e
