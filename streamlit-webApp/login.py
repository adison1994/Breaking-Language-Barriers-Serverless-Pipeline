import boto3
import time
from datetime import datetime, timedelta
from credentials import get_credentials



user_pool_id, app_client_id, app_client_secret = get_credentials()

client = boto3.client('cognito-idp')
region = 'us-east-1'
dynamodb_client = boto3.client('dynamodb', region_name = region)
user_pl_id= user_pool_id
app_cli_id= app_client_id
authorized = False
username = ''
IdToken = ''


def authorize_user(username, password):

	try:
		cognito_resp = client.admin_initiate_auth(
            UserPoolId=user_pl_id,
            ClientId=app_cli_id,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password
                }
            )
	    
		AccessToken=str(cognito_resp['AuthenticationResult']['AccessToken'])
		RefreshToken=str(cognito_resp['AuthenticationResult']['RefreshToken'])
		IdToken=str(cognito_resp['AuthenticationResult']['IdToken'])
		expiration=cognito_resp['AuthenticationResult']['ExpiresIn']

		expire_time = datetime.now() + timedelta(seconds=expiration)
		expire_time = expire_time.strftime("%Y-%m-%d %H:%M:%S")


		
		add_to_db = dynamodb_client.put_item(
	            TableName = 'NERUserTokens',Item = {

	            'CurrentUser' : {'S': str(username)},
	            'IdToken' : {'S':IdToken},
	            'RefreshToken' : {'S':RefreshToken},
	            'AccessToken' : {'S':AccessToken},
	            'TokenTime' : {'S':expire_time}
	            })
		if cognito_resp['AuthenticationResult']['AccessToken']:
			if(cognito_resp['ResponseMetadata']['HTTPStatusCode'] == 200):
				authorized = True
				return authorized, username, IdToken
	    
	except:
	    authorized = False 
	    return authorized, username, IdToken



    