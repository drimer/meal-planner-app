provider "aws" {
  region = "us-west-2"
}

resource "aws_dynamodb_table" "meal_planner" {
  name           = var.dynamodb_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "key"
  attribute {
    name = "key"
    type = "S"
  }
}

resource "aws_lambda_function" "meal_planner" {
  function_name = "meal_planner_lambda"
  runtime       = "python3.8"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "lambda_function.lambda_handler"
  filename      = "backend.zip"

  environment {
    variables = {
      DYNAMODB_TABLE = aws_dynamodb_table.meal_planner.name
    }
  }
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })

  inline_policy {
    name = "lambda_policy"
    policy = jsonencode({
      Version = "2012-10-17",
      Statement = [
        {
          Action = [
            "dynamodb:*",
            "logs:*",
          ],
          Effect   = "Allow",
          Resource = "*"
        },
      ]
    })
  }
}