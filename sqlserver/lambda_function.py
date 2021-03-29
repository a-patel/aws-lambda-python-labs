import boto3
import botocore
import json
import logging
import os
import pyodbc


log = logging.getLogger()
log.setLevel(logging.INFO)


def lambda_handler(event, context):
    log.debug('Event: %s', event)
    print("Received event: " + json.dumps(event, indent=2))
    

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=server_name;'
                          'Database=db_name;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM db_name.Table')

    for row in cursor:
        print(row)

    # TODO: DO YOUR WORK


    return 0