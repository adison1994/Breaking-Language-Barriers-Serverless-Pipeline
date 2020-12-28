import boto3
from botocore.config import Config
import logging
import time
import ast
import json

region = ''
client = boto3.client('transcribe', region_name = region)
s3_client = boto3.client('s3', region_name = region)
bucket_1 = ''
bucket_2 = ''



def check_transcribe_status(Transcription_Job_Name):
	status = ''
	status_resp = client.get_transcription_job(TranscriptionJobName = Transcription_Job_Name)
	if (status_resp['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED'):
		status = 'COMPLETED'
	else: #(status_resp['TranscriptionJob']['TranscriptionJobStatus'] == 'IN_PROGRESS'):
		status = 'IN_PROGRESS'
	return status

def get_transcription(transcribe_job_file, username):
	time.sleep(10)
	s3_file_path = 'JobFiles/{}'.format(transcribe_job_file)
	response = s3_client.get_object(Bucket=bucket_2, Key=s3_file_path)
	file_content = response['Body'].read().decode('utf-8')
	json_content = json.loads(file_content)
	text = json_content['results']['transcripts'][0]['transcript']

	timestr = time.strftime("%Y%m%d-%H%M%S")
	transcribe_f_tmp = "/tmp/" + username + "_transcribed_text_" + timestr + '.txt'
	transcribe_f = username + "_transcribed_text_" + timestr + '.txt'

	with open(transcribe_f_tmp, 'w', encoding='utf-8') as transcript:
		transcript.write(text)
	transcript.close()
	
	response = s3_client.upload_file(Filename=transcribe_f_tmp, Bucket=bucket_2, Key='English/{}'.format(transcribe_f))
		
	return transcribe_f



def lambda_handler(event, context):
	
	try:
		TranslationorNER = ''
		Username = event['body']['Username']
		Langauges = ast.literal_eval(event['body']['Langauges'])
		User_selection_map = ast.literal_eval(event['body']['User_selection_map'])
		Podcast_map = ast.literal_eval(event['body']['Podcast_map'])
		Summarize = User_selection_map['Summarize']

		Transcription_Job_Name = event['body']['Transcription_Job_Name']
		Transcribe_job_file = event['body']['Transcribe_job_file']

		TranscibeStatus = check_transcribe_status(Transcription_Job_Name)

		if(TranscibeStatus == 'COMPLETED'):
			Transcribe_file = get_transcription(Transcribe_job_file, Username)
			Podcast_map['Transcribe_file'] = Transcribe_file
			TranslationorNER = User_selection_map['TranslationorNER']
		
		return {
            "body":{
                "TranslationorNER": TranslationorNER,
                "Podcast_map": str(Podcast_map),
	            "User_selection_map": str(User_selection_map), 
                "Langauges":str(Langauges),
                "Username": Username,
                "TranscibeStatus": TranscibeStatus,
                "Summarize": Summarize,
                "Transcribe_job_file": Transcribe_job_file,
                "Transcription_Job_Name": Transcription_Job_Name

            }
        }
	except Exception as e:
		logging.error('Exception: %s. Unable to Scrape Audio files' % e)
		raise e
