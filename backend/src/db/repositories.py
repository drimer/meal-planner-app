import os

import boto3
from botocore.exceptions import ClientError
from db.models import Ingredient


class IngredientRepository:
    __TABLE_NAME = "ingredients"

    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb", endpoint_url=os.getenv("DYNAMODB_ENDPOINT"))
        self.table = self.dynamodb.Table(self.__TABLE_NAME)

    def get_by_name(self, name: str) -> Ingredient:
        try:
            response = self.table.query(
                IndexName="name-index",
                KeyConditionExpression=boto3.dynamodb.conditions.Key("name").eq(name),
            )
            if response["Items"]:
                return Ingredient.from_dict(response["Items"][0])
            else:
                return None
        except ClientError as e:
            print(f"Failed to get ingredient by name: {e.response['Error']['Message']}")
            return None

    def get_by_uuid(self, uuid: str) -> Ingredient:
        try:
            response = self.table.get_item(Key={"uuid": uuid})
            if "Item" in response:
                return Ingredient.from_dict(response["Item"])
            else:
                return None
        except ClientError as e:
            print(f"Failed to get ingredient by UUID: {e.response['Error']['Message']}")
            return None

    def get_all(self) -> list[Ingredient]:
        try:
            response = self.table.scan()
            return [Ingredient.from_dict(item) for item in response["Items"]]
        except ClientError as e:
            print(f"Failed to get all ingredients: {e.response['Error']['Message']}")
            return []

    def create(self, ingredient: Ingredient) -> Ingredient:
        try:
            self.table.put_item(Item=ingredient.to_dict())
            return ingredient
        except ClientError as e:
            print(f"Failed to insert ingredient: {e.response['Error']['Message']}")
            return None
