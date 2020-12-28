import boto3
from botocore.config import Config
import logging
import time
import ast
import json
import random

region = ''
client = boto3.client('transcribe', region_name = region)
s3_client = boto3.client('s3', region_name = region)
bucket_1 = ''
bucket_2 = ''


def get_audio_transcript(username, scrape_audio_f):
	
	rand = random.randint(1, 1000)
	audio_file_uri = 's3://' + bucket_1 + '/English/{}'.format(scrape_audio_f)
	timestr = time.strftime("%Y%m%d-%H%M%S")
	Transcription_Job_Name = username + "_transcribe_job_" + timestr + str(rand)

	timestr = time.strftime("%Y%m%d-%H%M%S")
	transcript_file = username + "_transcribe_" + timestr + str(rand) + '.json'

	response = client.start_transcription_job(
    TranscriptionJobName=Transcription_Job_Name,
    LanguageCode='en-US',
    MediaFormat='mp3',
    Media={
        'MediaFileUri': audio_file_uri
    },
    OutputBucketName=bucket_2,
    OutputKey= 'JobFiles/{}'.format(transcript_file)
	)	

	return transcript_file, Transcription_Job_Name


def lambda_handler(event, context):
	
	try:
		
		Username = event['body']['Username']
		Langauges = ast.literal_eval(event['body']['Langauges'])
		User_selection_map = ast.literal_eval(event['body']['User_selection_map'])
		Podcast_map = ast.literal_eval(event['body']['Podcast_map'])

		Podcast_audio = Podcast_map['Scraped_podcast']
		Transcribe_job_file, Transcription_Job_Name = get_audio_transcript(Username, Podcast_audio)	

		return {
            "body":{
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
