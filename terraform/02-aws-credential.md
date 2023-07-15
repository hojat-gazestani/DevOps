# aws provider

```shell
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region     = "us-west-2"
  access_key = "my-access-key"
  secret_key = "my-secret-key"
}
terraform plan
```

# or

```shell
export AWS_ACCESS_KEY_ID="anaccesskey"
export AWS_SECRET_ACCESS_KEY="asecretkey"
export AWS_REGION="us-west-2"
```

# or

```shell
aws configure
> cat ~/.aws/credentials
[default]
aws_access_key_id = "anaccesskey"
aws_secret_access_key = "asecretkey"

> cat ~/.aws/config
[default]
region = eu-west-2
```