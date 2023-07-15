#  variable

![vaiable](https://github.com/hojat-gazestani/DevOps/blob/main/terraform/pic/02-variable.png)
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
vim variable.tf
variable "ami_id" {
  default = "ami-0507f77897697c4ba"
}
variable "instance_type" {
  default = "t2.nano"
}
variable "key_name" {
  default = "sword"
}
```