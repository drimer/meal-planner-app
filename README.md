# Meal Planner App

This project is a meal planner application that helps users plan their meals for 4 weeks. It includes a backend written in Python using AWS Lambda and DynamoDB, and a frontend written in Flutter.

## Getting Started

### Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/)
- [Terraform](https://www.terraform.io/downloads.html)
- [Flutter](https://flutter.dev/docs/get-started/install)

### Backend

1. Navigate to the `backend` directory:

    ```sh
    cd backend
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the tests:

    ```sh
    pytest
    ```

4. Ensure you have Docker installed and run all the infrastucture:

    ```sh
    docker-compose up
    ```

5. Ensure you have AWS_PROFILE set and its corresponding entry in ~/.aws/credentials

### Frontend

1. Navigate to the `frontend` directory:

    ```sh
    cd frontend
    ```

2. Get the Flutter dependencies:

    ```sh
    flutter pub get
    ```

3. Run the app locally:

    ```sh
    flutter run
    ```

### Infrastructure

1. Navigate to the `infra` directory:

    ```sh
    cd infra
    ```

2. Initialize Terraform:

    ```sh
    terraform init
    ```

3. Apply the Terraform configuration:

    ```sh
    terraform apply
    ```

## Configuration

- **Database connection string**: Configure the DynamoDB table name in `infra/variables.tf`.
- **First day of the week**: To configure the first day of the week, update the relevant configuration in the frontend (this feature is to be implemented in the Flutter app).

## Deployment

1. Zip the backend files:

    ```sh
    cd backend
    zip -r ../backend.zip .
    ```

2. Deploy the backend and frontend using Terraform:

    ```sh
    cd ../infra
    terraform apply
    ```

## Running Unit Tests

### Backend

To run the backend unit tests, navigate to the `backend` directory and run:

```sh
pytest