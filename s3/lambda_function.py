import boto3
import botocore
import json
import logging
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image


log = logging.getLogger()
log.setLevel(logging.INFO)

s3_client = boto3.client('s3')


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(resized_path)

    
def lambda_handler(event, context):
    log.debug('Event: %s', event)
    print("Received event: " + json.dumps(event, indent=2))

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        log.info('Reading {} from {}'.format(key, bucket))
        

        # Resize image
        tmpkey = key.replace('/', '')
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        upload_path = '/tmp/resized-{}'.format(tmpkey)
        s3_client.download_file(bucket, key, download_path)
        resize_image(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)


        # Read CSV file
        # move to separate function
        csvfile = s3_client.get_object(Bucket=bucket, Key=key)
        lines = csvfile['Body'].read().split(b'\n')
        for line in lines:
            log.info(line.decode())
            content = content + '\n' + line.decode()
        log.info(content)


        # TODO: DO MORE WORK


    return 0





# Ref: https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html