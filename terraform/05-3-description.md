# Always use description

![description](https://github.com/hojat-gazestani/DevOps/blob/main/terraform/pic/04-description.png)

```shell
vim main.tf
resource "aws_instance" "trtest" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    terraform = "test"
    name      = "trtest"
  }
}
```

```shell
variable "ami_id" {
  description = "this is ami_id"
}
variable "instance_type" {
  description = "this is instanse type"
}
variable "key_name" {
  description = "this is key name"
}
```

```shell
vim terraform.tfvars
ami_id        = "ami-0507f77897697c4ba"
instance_type = "t2.nano"
key_name      = "sword"
```

