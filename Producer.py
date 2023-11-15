## Producer file (will be migrated into Lambda function)

import json
import boto3

sqs = boto3.client('sqs')
def createHandler(event):
    sqs.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/675489061989/cs5260-requests',
        MessageBody=json.dumps(event)
        )
    
    

def updateHandler(event):
    pass

def deleteHandler(event):
    pass



def lambda_handler(event, context):
    
    response = {'statusCode': 422,
        'body': "Type not present in request..."
    }
    if 'Type' in event:
        if event['Type'] == "Create":
            createHandler(event)
            
        if event['Type'] == "Delete":
            deleteHandler(event)
            
        if event['Type'] == "Update":
            deleteHandler(event)
        
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': event['Type']}),
        }

    return response

