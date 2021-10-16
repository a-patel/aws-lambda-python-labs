import boto3
import botocore
import json
import logging
import os


log = logging.getLogger()
log.setLevel(logging.INFO)


email_from = 'from@example.com'
email_to = 'to@example.com'
email_cc = 'cc@example.com'
emaiL_subject = 'Subject'
email_body = 'This is test email.'

def lambda_handler(event, context):
    log.debug('Event: %s', event)
    print("Received event: " + json.dumps(event, indent=2))
    

    ses = boto3.client('ses')

    response = ses.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to,
            ],
            'CcAddresses': [
                email_cc,
            ]
        },
        Message={
            'Subject': {
                'Data': emaiL_subject
            },
            'Body': {
                'Text': {
                    'Data': email_body
                }
            }
        }
    )

    return 0