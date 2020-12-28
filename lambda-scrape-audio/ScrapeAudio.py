import boto3
import logging
import ast
import time
import urllib.request

region = ''
s3_client = boto3.client('s3', region_name = region)
bucket_name = ''


def get_podcast_audio(audio_links, username,languages, gender):
	scraped_audio_map = {}
	scraped_podcasts = []
	for link_a in audio_links:
		timestr = time.strftime("%Y%m%d-%H%M%S")
		scrape_audio_tmp = "/tmp/" + username + "_scraped_audio_" + timestr + '.mp3'
		scrape_audio = username + "_scraped_audio_" + timestr + '.mp3'
		audio = urllib.request.urlretrieve(link_a, scrape_audio_tmp)

		response = s3_client.upload_file(Filename=scrape_audio_tmp, Bucket=bucket_name, Key='English/{}'.format(scrape_audio))
		scraped_podcasts.append(scrape_audio)

	scraped_audio_map['scraped_podcasts'] = scraped_podcasts

	return scraped_audio_map




def lambda_handler(event, context):

	try:
		Username = event['body']['Username']
		Langauges = ast.literal_eval(event['body']['Langauges'])
		User_selection_map = ast.literal_eval(event['body']['User_selection_map'])
		Podcasts_links = ast.literal_eval(event['body']['Podcasts_links'])
		
		Scraped_audio_map = get_podcast_audio(Podcasts_links, Username, Langauges, User_selection_map['Gender'])
		
		return {
            "body":{
                "User_selection_map": str(User_selection_map), 
                "Langauges":str(Langauges),
                "Username": Username,
                "Podcasts_links": str(Podcasts_links),
                "Scraped_audio_map": str(Scraped_audio_map)                           
            }
        }
	except Exception as e:
		logging.error('Exception: %s. Unable to Scrape Audio files' % e)
		raise e
