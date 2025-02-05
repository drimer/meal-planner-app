import json
import boto3
import os

# Initialize DynamoDB resource
print('Conneting to DynaoDB on endpoint:', os.getenv('DYNAMODB_ENDPOINT'), ' and region:', os.getenv('AWS_REGION'))
dynamodb = boto3.resource('dynamodb', endpoint_url=os.getenv('DYNAMODB_ENDPOINT'))
table = dynamodb.Table('table')

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
    
    
if __name__ == '__main__':
    event = {
        'httpMethod': 'POST',
        'body': '{"name": "Chicken Breast", "serving": 200, "serving_unit": "g", "calories_per_serving": 165, "protein_per_serving": 31}'
    }
    response = lambda_handler(event, None)
    print(response)
    
    event = {
        'httpMethod': 'GET',
        'queryStringParameters': {'key': 'Chicken Breast'}
    }
    response = lambda_handler(event, None)
    print(response)