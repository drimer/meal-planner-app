import pytest
from lambda_function import lambda_handler

def test_create_item():
    event = {
        'httpMethod': 'POST',
        'body': '{"name": "Chicken Breast", "serving": 200, "serving_unit": "g", "calories_per_serving": 165, "protein_per_serving": 31}'
    }
    response = lambda_handler(event, None)
    assert response['statusCode'] == 200

def test_get_item():
    event = {
        'httpMethod': 'GET',
        'queryStringParameters': {'key': 'Chicken Breast'}
    }
    response = lambda_handler(event, None)
    assert response['statusCode'] == 200