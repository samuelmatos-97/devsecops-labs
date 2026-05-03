provider "aws" {
  region = "eu-west-1"
}

resource "aws_instance" "lab06_instance" {
  ami           = "ami-08f9a9c699d2ab3f9"
  instance_type = "t2.micro"

  tags = {
    Name = "lab06-terraform-instance"
  }
}
