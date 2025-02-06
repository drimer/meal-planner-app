import json
from decimal import Decimal

from db.models import Ingredient
from db.repositories import IngredientRepository

INGREDIENT_REPOSITORY = IngredientRepository()


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        if isinstance(obj, Ingredient):
            return obj.__dict__

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
    # item = INGREDIENT_REPOSITORY.get_by_name(name)
    items = INGREDIENT_REPOSITORY.get_all()
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
