![Banner image](https://assets-global.website-files.com/63c6be5d69abf87798adedb7/654bd4d5387a55ba07dad30b_banner_yolov8_lambda-p-1600.jpg)

# HowTo: Deploying YOLOv8 on AWS Lambda

This repository contains code and instructions for deploying YOLOv8 on AWS Lambda. The accompanying blog post, "HowTo: Deploying YOLOv8 on AWS Lambda," can be found [here](https://www.trainyolo.com/blog/deploy-yolov8-on-aws-lambda).

## Requirements

Before you begin, make sure you have the following requirements installed:

- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- Docker (optionally): if you want to build your Lambda deployment package within a Docker container, otherwise make sure you have the same python version as indicated in the template.yaml file.

## Getting Started

Follow these steps to get started with deploying YOLOv8 on AWS Lambda:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/trainyolo/YOLOv8-aws-lambda
```

2. Place your YOLOv8 ONNX model in the lambda-codebase/models directory within the cloned repository.

3. In the lambda-codebase/app.py file, change the name of the YOLOv8 model to match the filename of the model you placed in the models directory.

4. Deploy the project using AWS SAM:

```bash
sam build --use-container
sam deploy --guided
```
Follow the prompts to deploy your YOLOv8 model on AWS Lambda.

## Testing the API Endpoint

To test the API endpoint, follow these steps:

In the test/test_api.py file, change the URL to match the endpoint of your deployed AWS Lambda function.

Run the test script:

```bash
python test/test_api.py
```

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or feedback, you can reach out to davy@trainyolo.com


