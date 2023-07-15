# terraform init plan apply

- Create provider file
```shell
vim provider.tf
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
}
```

- Create main file

```shell
vim main.tf
resource "aws_instance" "trtest" {
  ami           = "ami-0507f77897697c4ba"
  instance_type = "t2.nano"

  tags = {
    terraform = "test"
  }
}
```

- run terraform

```shell
terraform init
terraform plan
terraform apply
terraform destory
```