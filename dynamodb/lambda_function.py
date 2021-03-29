import boto3
import botocore
import json
import logging
import os


log = logging.getLogger()
log.setLevel(logging.INFO)


dynamodb_client = boto3.resource('dynamodb')
TABLE = "customer"


# Scans table and return results
def scan_table(table):
    log.info(f"Scanning Table {table}")
    customer_table = dynamodb_client.Table(table)
    response = customer_table.scan()
    items = response['Items']
    log.info(f"Found {len(items)} Items")
    return items


def lambda_handler(event, context):
    log.debug('Event: %s', event)
    print("Received event: " + json.dumps(event, indent=2))
    
    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        # TODO: DO YOUR WORK
    
    print('Successfully processed %s records.' % str(len(event['Records'])))


    return 0