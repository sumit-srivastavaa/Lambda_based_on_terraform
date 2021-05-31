import requests
import boto3
import json



url = 'https://website.com'
region_name = 'us-east-1'
secret_name = 'schedules-secrets'
username = 'username'
proxy = 'http://my-proxy.vpc.com'



# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(service_name='secretsmanager',  region_name=region_name)
        
get_secret_value_response = client.get_secret_value(SecretId=secret_name)
            print(get_secret_value_response)
         'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                j = json.loads(secret)
                API_KEY = j['key']
                print(API_KEY)
        
        
        r = requests.get('url', auth=(username, API_KEY),proxies=proxy) 

