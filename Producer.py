## Producer file (will be migrated into Lambda function)

import json
import boto3

sqs = boto3.client('sqs')


def serializeData(data):
    return json.dumps(data)

def requirementsCheck(data):
    if "owner" not in data:
        return False
        
    if 'requestId' not in data:
        return False
        
    if 'widgetId' not in data:
        return False
    
    return True



def createHandler(event):
    if requirementsCheck(event):
        
        message = serializeData(event)
        sqs.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/675489061989/cs5260-requests',
            MessageBody=message
            )
        return True
    return False
    

def updateHandler(event):
    if requirementsCheck(event):
        
        message = serializeData(event)
        sqs.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/675489061989/cs5260-requests',
            MessageBody=message
            )
        return True
    return False

def deleteHandler(event):
    if requirementsCheck(event):
        
        message = serializeData(event)
        sqs.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/675489061989/cs5260-requests',
            MessageBody=message
            )
        return True
    return False



def lambda_handler(event, context):

    response = {"statusCode": 400,"headers": {
        "Content-Type": "application/json"},
        'body': "Bad Request"}
    newEvent = {}
    if 'body' in event:
        newEvent = json.loads(event['body'])
    else:
        newEvent = event

    if 'type' in newEvent:
        try:
            successful = False
            if newEvent['type'] == "create":
                if createHandler(newEvent):
                    successful = True
                
            if newEvent['type'] == "delete":
                if deleteHandler(newEvent):
                    successful = True
                
            if newEvent['type'] == "update":
                if updateHandler(newEvent):
                    successful = True
            if successful:
                response = {
                    'statusCode': 200,"headers": {
        "Content-Type": "application/json"},
        'body':"Success"}
    
        except Exception as e:
            return {
            'statusCode': 500,"headers": {
        "Content-Type": "application/json"
    },
            'body': str(e),
        }
    else:
        response = {'statusCode': 422,"headers": {
                    "Content-Type": "application/json"},
                    'body':"Type not present in request"
                }
                
        return response
    

    return response