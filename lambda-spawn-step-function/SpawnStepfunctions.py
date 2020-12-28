import boto3 
import time
import urllib.request
from boto3.dynamodb.conditions import Key, Attr
import time
import logging
import ast
import json

region = ''
#s3_client = boto3.resource('s3', region_name = region)
s3_client = boto3.client('s3', region_name = region)
bucket_name = ''
sf_client = boto3.client('stepfunctions')




def invoke_child_step_function(podcast_file, Username, Langauges, User_selection_map, count):
	time.sleep(1)
	timestr = time.strftime("%Y%m%d-%H%M%S")
	sf_name = Username + '_CSFE_' + timestr + str(count)
	Podcast_map = {}
	Podcast_map['Scraped_podcast'] = podcast_file
	Podcast_map['Sf_Execution'] = sf_name
	sf_input = json.dumps({"body": {"Podcast_map": str(Podcast_map),
	               "User_selection_map": str(User_selection_map), 
                	"Langauges":str(Langauges),
                	"Username": Username
	               }}, sort_keys=True)

	response = sf_client.start_execution(
		stateMachineArn='arn:aws:states:us-east-1:165885578631:stateMachine:BreakingBarriersMachine',
		name=sf_name,
		input= sf_input)

	return sf_name


def spawn_step_function(Scraped_audio_map, Username, Langauges, User_selection_map):
	stepfunct_exec_list = []
	count = 0
	if User_selection_map['ScrapeorNot'] == 'Yes':
		for podcast in Scraped_audio_map['scraped_podcasts']:
			count += 1
			sf_name = invoke_child_step_function(podcast, Username, Langauges, User_selection_map, count)
			stepfunct_exec_list.append(sf_name)
	elif User_selection_map['ScrapeorNot'] == 'No':
		for podcast in Scraped_audio_map['uploaded_podcasts']:
			count += 1
			sf_name = invoke_child_step_function(podcast, Username, Langauges, User_selection_map, count)
			stepfunct_exec_list.append(sf_name)
        
	return stepfunct_exec_list


def lambda_handler(event, context):

	try:
		
		Username = event['body']['Username']
		Langauges = ast.literal_eval(event['body']['Langauges'])
		User_selection_map = ast.literal_eval(event['body']['User_selection_map'])
		Podcasts_links = ast.literal_eval(event['body']['Podcasts_links'])
		Scraped_audio_map = ast.literal_eval(event['body']['Scraped_audio_map'])

		SF_ME_list = spawn_step_function(Scraped_audio_map, Username, Langauges, User_selection_map)
		
		return {
            "body":{
                "User_selection_map": str(User_selection_map), 
                "Langauges":str(Langauges),
                "Username": Username,
                "Podcasts_links": str(Podcasts_links),
                "Scraped_audio_map": str(Scraped_audio_map),
                "Stepfunct_Master_list": str(SF_ME_list)                           
            }
        }
	except Exception as e:
		logging.error('Exception: %s. Unable to Scrape Audio files' % e)
		raise e


