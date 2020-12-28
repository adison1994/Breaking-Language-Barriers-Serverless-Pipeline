import boto3 
from botocore.config import Config

polly_client = boto3.client('polly', config=Config(
    region_name='us-east-1'))

def get_welcome_msg(uname):
	text = "Welcome" + uname + ", You Have successfully Logged In. You can now start using Services offered by Breaking Language Barriers"
	response = polly_client.synthesize_speech(Text=text, VoiceId='Joanna', OutputFormat='mp3')
	audio_bytes = response['AudioStream'].read()
	return audio_bytes
