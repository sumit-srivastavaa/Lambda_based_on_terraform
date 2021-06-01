import requests
import boto3
import json
import base64
from botocore.exceptions import ClientError



url = 'https://bustime.mta.info/api/where/stops-for-location.json'
#region_name = 'us-east-1'
#secret_name = 'schedules-secrets'
#username = 'username'
#PROXY_URL = 'http://my-proxy.vpc.com'
#API_KEY = 'b3d8aa55-42c0-4faf-9195-39c7696f4dbf'


def get_secret():
            secret_name = "API_SECRETS"
            region_name = "us-east-1"
        
            #create secret manager client
            session = boto3.session.Session()
            client = session.client(
            service_name='secretsmanager',
            region_name=region_name
            )
    
    ##checking for exceptions
            try:
                get_secret_value_response = client.get_secret_value(
                   SecretId=secret_name
                )
            except ClientError as e:
                if e.response['Error']['Code'] == 'DecryptionFailureException':
                   raise e
        
        
                elif e.response['Error']['Code'] == 'InternalServiceErrorException':
                     raise e
        
        
                elif e.response['Error']['Code'] == 'InvalidParameterException':
                     raise e
        
        
                elif e.response['Error']['Code'] == 'InvalidRequestException':
                     raise e
        
        
                elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                     raise e
            else:
        
        
                if 'SecretString' in get_secret_value_response:
                    secret = get_secret_value_response['SecretString']
                else:
                
                     secret = base64.b64decode(get_secret_value_response['SecretBinary'])
                return json.loads(secret)




###requesting API with Key 
params = dict(key=API_KEY, lang='en-es')
res = requests.get(url, params=params)

#printing outputs
print(res.text)

json = res.json()
print(json)