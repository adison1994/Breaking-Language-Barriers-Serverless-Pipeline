import boto3
from botocore.config import Config
import logging
import time
import ast
import json



def wait_for_transcribe():
	time.sleep(10)
	

def lambda_handler(event, context):
	
	try:
		Username = event['body']['Username']
		Langauges = ast.literal_eval(event['body']['Langauges'])
		User_selection_map = ast.literal_eval(event['body']['User_selection_map'])
		Podcast_map = ast.literal_eval(event['body']['Podcast_map'])
		TranslationorNER = event['body']['TranslationorNER']

		Transcription_Job_Name = event['body']['Transcription_Job_Name']
		Transcribe_job_file = event['body']['Transcribe_job_file']
		
		wait_for_transcribe()
		return {
            "body":{"TranslationorNER": TranslationorNER,
                "Podcast_map": str(Podcast_map),
	            "User_selection_map": str(User_selection_map), 
                "Langauges":str(Langauges),
                "Username": Username,
                "Transcribe_job_file": Transcribe_job_file,
                "Transcription_Job_Name": Transcription_Job_Name
            }
        }
	except Exception as e:
		logging.error('Exception: %s. Unable to Scrape Audio files' % e)
		raise e
