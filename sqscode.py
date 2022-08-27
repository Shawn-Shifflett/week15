import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    sqs = boto3.client("sqs")
    sqs.send_message(
         QueueUrl="https://sqs.us-east-1.amazonaws.com/513843887415/time",MessageBody= time
        )
    return {
        'statusCode': 200,
        'body': "Congrats! Msg sent to SQS!"
    }
