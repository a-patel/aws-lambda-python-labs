import boto3
import botocore
import json
import logging
import os
import sys
import base64
from botocore.exceptions import ClientError

log = logging.getLogger()
log.setLevel(logging.INFO)

# global variables for re-use of invocations
session = boto3.session.Session()
secretName = "myapp/api/key"
secretRegion = "us-east-1"

# global variable to cut down the number of calls to AWS Secrets Manager
apiKey = ""


def lambda_handler(event, context):
    log.debug('Event: %s', event)
    print("Received event: " + json.dumps(event, indent=2))
    
    # pull the API key from AWS Secrets Manager
    # only reach out to grab key if it is an empty string
    if apiKey == "":
        apiKey = get_secret(secretName, secretRegion)['apikey']
    else:
        print("API Key is already set")
    

    # TODO: DO YOUR WORK


    return 0




def get_secret(secret_name: str, region_name: str):
    """
    Gets the secret from AWS Secrets Manager.
    
    Parameters:
        secret_name (str) = the name of the secret to get.
        region_name (str) = the name of the AWS region where the secret is.
        
    Returns:
        secret_val (dict) = the key-value pair of the secret.
    """
    
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return json.loads(secret)
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return json.loads(decoded_binary_secret)