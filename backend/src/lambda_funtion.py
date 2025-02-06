import json
import os
from decimal import Decimal

import boto3

# Initialize DynamoDB resource
print(
    "Conneting to DynaoDB on endpoint:",
    os.getenv("DYNAMODB_ENDPOINT"),
    " and region:",
    os.getenv("AWS_REGION"),
)
dynamodb = boto3.resource("dynamodb", endpoint_url=os.getenv("DYNAMODB_ENDPOINT"))
ingredients_table = dynamodb.Table("ingredients")


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def lambda_handler(event, context):
    if event["httpMethod"] == "POST":
        return create_item(event)
    elif event["httpMethod"] == "GET":
        return get_item(event)
    else:
        return {"statusCode": 405, "body": json.dumps("Method Not Allowed")}


def create_item(event):
    body = json.loads(event["body"])
    ingredients_table.put_item(Item=body)
    return {"statusCode": 200, "body": json.dumps("Item created")}


def get_item(event):
    name = event["queryStringParameters"]["name"]
    # response = ingredients_table.get_item(Key={"name": name})
    items = ingredients_table.scan()["Items"]
    return {"statusCode": 200, "body": json.dumps(items[0], cls=DecimalEncoder)}


if __name__ == "__main__":
    # event = {
    #     "httpMethod": "POST",
    #     "body": json.dumps(
    #         {
    #             "uuid": str(uuid.uuid4()),
    #             "name": "Chicken Breast",
    #             "serving": 200,
    #             "serving_unit": "g",
    #             "calories_per_serving": 165,
    #             "protein_per_serving": 31,
    #         }
    #     ),
    # }
    # response = lambda_handler(event, None)
    # print(response)

    event = {"httpMethod": "GET", "queryStringParameters": {"name": "Chicken Breast"}}
    response = lambda_handler(event, None)
    print(response)
