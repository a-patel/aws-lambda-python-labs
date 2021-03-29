import boto3
import botocore
import json
import logging
import os


log = logging.getLogger()
log.setLevel(logging.INFO)


QUEUE = "producer"
sqs_client = boto3.client("sqs")



def send_sqs_msg(msg, queue_name, delay=0):
    queue_url = sqs_client.get_queue_url(QueueName=queue_name)["QueueUrl"]
    queue_send_log_msg = "Send message to queue url: %s, with body: %s" % (queue_url, msg)
    log.info(queue_send_log_msg)
    json_msg = json.dumps(msg)
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json_msg,
        DelaySeconds=delay)
    queue_send_log_msg_resp = "Message Response: %s for queue url: %s" %\
        (response, queue_url) 
    log.info(queue_send_log_msg_resp)
    return response


def delete_sqs_msg(queue_name, receipt_handle):
    try:
        queue_url = sqs_client.get_queue_url(QueueName=queue_name)["QueueUrl"]
        delete_log_msg = "Deleting msg with ReceiptHandle %s" % receipt_handle
        log.info(delete_log_msg)
        response = sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
    except botocore.exceptions.ClientError as error:
        exception_msg = "FAILURE TO DELETE SQS MSG: Queue Name [%s] with error: [%s]" %\
            (queue_name, error)
        log.exception(exception_msg)
        return None

    delete_log_msg_resp = "Response from delete from queue: %s" % response
    log.info(delete_log_msg_resp)
    return response


def lambda_handler(event, context):
    log.debug('Event: %s', event)
    print("Received event: " + json.dumps(event, indent=2))


    for record in event['Records']:
        message = record["body"]
        print("Message: " + str(message))
        # TODO: PROCESS MESSAGE
        


    return 0