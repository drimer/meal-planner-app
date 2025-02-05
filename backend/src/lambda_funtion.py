import json
import boto3
import os

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.getenv('DYNAMODB_TABLE'))

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        return create_item(event)
    elif event['httpMethod'] == 'GET':
        return get_item(event)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps('Method Not Allowed')
        }

def create_item(event):
    body = json.loads(event['body'])
    table.put_item(Item=body)
    return {
        'statusCode': 200,
        'body': json.dumps('Item created')
    }

def get_item(event):
    key = event['queryStringParameters']['key']
    response = table.get_item(Key={'key': key})
    return {
        'statusCode': 200,
        'body': json.dumps(response.get('Item', {}))
    }