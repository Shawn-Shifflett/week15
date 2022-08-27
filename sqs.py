import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(Queuename='Wanna know the current time?')

print(queue.url)
