import boto3 
import logging
import time
import ast
import json

region = ''
dynamodb_client = boto3.client('dynamodb', region_name = region)
ddb_table =''


def lambda_handler(event, context):
	
	try:
		NER_Masking_map = event['body']['NER_Masking_map']
		Username = event['body']['Username']
		Langauges = event['body']['Langauges']
		User_selection_map = event['body']['User_selection_map']
		Podcast_map = event['body']['Podcast_map']
		Transcribe_file = event['body']['Transcribe_file']
		TranslationorNER = event['body']['TranslationorNER']
		Summarize = event['body']['Summarize']
		OutputAudio = event['body']['OutputAudio']
		Gender = event['body']['Gender']
		Audio_trans_map = event['body']['Audio_trans_map']
		audio_summ_trans_map = event['body']['audio_summ_trans_map']
		Text_trans_map = event['body']['Text_trans_map']
		Summary_txt_trans_map = event['body']['Summary_txt_trans_map']
		Sf_Execution = event['body']['Sf_Execution']


		data = {
                'Child_Step_function_Execution': {
                    'S': Sf_Execution
                },
                'Username': {
                    'S': Username
                },
                'NER_Masking_map': {
                    'S': NER_Masking_map
                },
                'Langauges': {
                    'S': Langauges
                },
                'User_selection_map': {
                    'S': User_selection_map
                },
                'Podcast_map': {
                    'S': Podcast_map
                },
                'Transcribe_file': {
                    'S': Transcribe_file
                },
                'Gender':{
                    'S': Gender
                },
                'TranslationorNER': {
                    'S': TranslationorNER
                },
                'Summarize': {
                    'S': Summarize
                },
                'OutputAudio': {
                    'S': OutputAudio
                },
                'Audio_trans_map': {
                    'S': Audio_trans_map
                },
                'audio_summ_trans_map': {
                    'S': audio_summ_trans_map
                },
                'Text_trans_map': {
                    'S': Text_trans_map
                },
                'Summary_txt_trans_map': {
                    'S': Summary_txt_trans_map
                }
            }

		data_j = json.dumps(data)

		meta_data = json.loads(data_j)

		dynamodb_client.put_item(
            TableName=ddb_table,
            Item=meta_data
        )

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
                "Summarize": Summarize,
                "OutputAudio": OutputAudio,
                "NER_Masking_map": str(NER_Masking_map),
                "Audio_trans_map": str(Audio_trans_map),
                "audio_summ_trans_map":str(audio_summ_trans_map)

            }
        }
	except Exception as e:
		logging.error('Exception: %s. Unable to Scrape Audio files' % e)
		raise e
