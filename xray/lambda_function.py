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
    

    # TODO: DO YOUR WORK


    return 0