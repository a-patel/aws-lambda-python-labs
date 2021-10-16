import boto3
import botocore
import json
import logging
import os


log = logging.getLogger()
log.setLevel(logging.INFO)


def lambda_handler(event, context):
    log.debug('Event: %s', event)
    print("Received event: " + json.dumps(event, indent=2))

    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name='/Prod/Db/Password', WithDecryption=True)
    print(parameter['Parameter']['Value'])

    return 0