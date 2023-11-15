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
    
    response = {'statusCode': 422,
        'body': "Type not present in request..."
    }
    if 'type' in event:
        try:
            successful = False
            if event['type'] == "create":
                if createHandler(event):
                    successful = True
                
            if event['type'] == "delete":
                if deleteHandler(event):
                    successful = True
                
            if event['type'] == "update":
                if updateHandler(event):
                    successful = True
            if successful:
                response = {
                    'statusCode': 200,
                    'body': json.dumps({'message': "Correctly sent request"}),
                }
            else:
                response = {'statusCode': 422,
                    'body': "Required Body not given."
                }
            return response
        except Exception as e:
            return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'}),
        }

    return response