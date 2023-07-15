# terraform.tfvar.tf

![tfvar](https://github.com/hojat-gazestani/DevOps/blob/main/terraform/pic/03-tfvar.png)

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

}
variable "instance_type" {

}
variable "key_name" {

}
```

```shell
vim terraform.tfvar
ami_id        = "ami-0507f77897697c4ba"
instance_type = "t2.nano"
key_name      = "sword"
```