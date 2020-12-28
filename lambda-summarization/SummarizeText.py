import boto3
from botocore.config import Config
import logging
import time
import ast
import json
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


region = ''
s3_client = boto3.client('s3', region_name = region)
bucket_1 = ''
bucket_2 = ''


def summarize_transcripts(transcribe_file, username):
	
	s3_file_path = '{}'.format(transcribe_file)
	response = s3_client.get_object(Bucket=bucket_1, Key=s3_file_path)
	document = response['Body'].read().decode('utf-8')

	# Object of automatic summarization.
	auto_abstractor = AutoAbstractor()
	auto_abstractor.tokenizable_doc = SimpleTokenizer()
	auto_abstractor.delimiter_list = [".", "\n"]
	abstractable_doc = TopNRankAbstractor()
	result_dict = auto_abstractor.summarize(document, abstractable_doc)
	summary_l = []
	for sentence in result_dict["summarize_result"]:
		summary_l.append(sentence)
	summarize_text = ''
	
	for i in range(0, len(summary_l)):
	    summarize_text += "".join(summary_l[i])

	timestr = time.strftime("%Y%m%d-%H%M%S")
	summ_text_f_tmp = "/tmp/" + username + "_summy_text_" + timestr + '.txt'
	summ_text_f = username + "_summy_text_" + timestr + '.txt'
	with open(summ_text_f_tmp, 'w', encoding="utf-8") as summy_f:
			summy_f.write(summarize_text)
	summy_f.close()
		
	summy_text_path = 'English/{}'.format(summ_text_f)
	response = s3_client.upload_file(Filename=summ_text_f_tmp, Bucket=bucket_2, Key=summy_text_path)
		

	return summ_text_f


def lambda_handler(event, context):
	
	try:
		Summarize = event['body']['Summarize']
		Username = event['body']['Username']
		Langauges = ast.literal_eval(event['body']['Langauges'])
		User_selection_map = ast.literal_eval(event['body']['User_selection_map'])
		Podcast_map = ast.literal_eval(event['body']['Podcast_map'])
		TranslationorNER = event['body']['TranslationorNER']
		Transcribe_file = Podcast_map['Transcribe_file']
		
		Summary_file = summarize_transcripts(Transcribe_file, Username)	
		Podcast_map['Summary_text_file'] = Summary_file
		
		return {
            "body":{
                "TranslationorNER": TranslationorNER,
                "Podcast_map": str(Podcast_map),
	            "User_selection_map": str(User_selection_map), 
                "Langauges":str(Langauges),
                "Username": Username,
                "Transcribe_file": Transcribe_file, 
                "Summarize": Summarize
            }
        }
	except Exception as e:
		logging.error('Exception: %s. Unable to Scrape Audio files' % e)
		raise e
