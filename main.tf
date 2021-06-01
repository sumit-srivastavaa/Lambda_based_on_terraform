provider "aws" {
  
  region = var.region
  access_key = var.access_key
  secret_key = var.saccesskey
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    },
    {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "secretsmanager:*",
            "Resource": "*"
        },
    {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action":[
                 "kms:Decrypt",
                 "kms:DescribeKey"
            "Resource": "ARN::"
        }
    
  ]
}
EOF
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "lambda_function_payload.zip"
  function_name = "lambda_function_name"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "exports.test"

  runtime = "python3.8"

  environment {
      
    variables = {secret_name = var.secretname, proxy = var.proxyname}
  }

resource "aws_kms_key" "secretkey" {

  name = "secrets-manager-key"
  description = "key for secret manager"
  enable_key_rotation = true


}

resource "aws_secretsmanager_secret" "secretmanager"{

  name = "API-SecretsManager"
  kms_key_id = secretkey.kms_key_id
  
}


}
