import boto3
import botocore.exceptions
import base64
import json
from credentials import get_credentials
import hmac
import hashlib



USER_POOL_ID, CLIENT_ID, APP_CLIENT_SECRET = get_credentials()


client = boto3.client('cognito-idp')
sign = False
message = ''


def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(APP_CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2



def user_signup(name, username, email, password):
    sign = False   
    resp = client.sign_up(
            ClientId= CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            Password=password, 
            UserAttributes=[
            {
                'Name': "name",
                'Value': name
            },
            {
                'Name': "email",
                'Value': email
            }
            ],
            ValidationData=[
                {
                'Name': "email",
                'Value': email
            },
            {
                'Name': "custom:username",
                'Value': username
            }
        ])



def confirm_signup(username, code):
    message = ''
    sign = False
    try:
        response = client.confirm_sign_up(
        ClientId=CLIENT_ID,
        SecretHash=get_secret_hash(username),
        Username=username,
        ConfirmationCode=code,
        ForceAliasCreation=False
       )
        sign = True
        message = 'You have been successfully signed up'
    except:
        message = 'Username or Email already exists'
    return message, sign