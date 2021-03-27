import json
import logging


log = logging.getLogger()
log.setLevel(logging.INFO)


def lambda_handler(event, context):
    log.debug('Event: %s', event)
    # print("Received event: " + json.dumps(event, indent=2))
    
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)

    # TODO: do your work

    return message