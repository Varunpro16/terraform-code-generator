import os

# Define the input Terraform configuration as a string
terraform_code = """

  
```hcl
// provider.tf

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.0"
    }
  }
  required_version = ">= 1.0.0"
}

provider "aws" {
  region = var.region
}
```

```hcl
// variables.tf

variable "region" {
  description = "The AWS region to create resources in."
}

variable "ami" {
  description = "The AMI ID for the EC2 instance."
}

variable "instance_type" {
  description = "The EC2 instance type."
}

variable "subnet_id" {
  description = "The ID of the subnet where the EC2 instance will be deployed."
}

variable "vpc_id" {
  description = "The ID of the VPC."
}

variable "security_group_name" {
  description = "The name of the security group."
}

variable "availability_zone" {
  description = "The availability zone of the subnet."
}

variable "ebs_volume_size" {
  description = "The size of the EBS volume in GiB."
}

variable "ebs_volume_type" {
  description = "The type of the EBS volume to be created."
}

variable "instance_name" {
  description = "The name tag for the EC2 instance."
}
```

```hcl
// key_pair.tf

resource "tls_private_key" "ec2_private_key" {
  algorithm = "RSA"
}

resource "aws_key_pair" "ec2_key_pair" {
  key_name   = "${var.instance_name}-key"
  public_key = tls_private_key.ec2_private_key.public_key_openssh
}

resource "local_file" "private_key_pem" {
  content     = tls_private_key.ec2_private_key.private_key_pem
  filename    = "${var.instance_name}_private_key.pem"
  file_permission = "0600"
}
```

```hcl
// security_group.tf

resource "aws_security_group" "ec2_security_group" {
  name        = var.security_group_name
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

```hcl
// ec2.tf

resource "aws_instance" "ec2_instance" {
  ami                         = var.ami
  instance_type               = var.instance_type
  subnet_id                   = var.subnet_id
  vpc_security_group_ids      = [aws_security_group.ec2_security_group.id]
  key_name                    = aws_key_pair.ec2_key_pair.key_name

  block_device {
    device_name = "/dev/sda1"
    volume_type = var.ebs_volume_type
    volume_size = var.ebs_volume_size
  }

  user_data = <<-EOF
              #!/bin/bash
              sed -i 's/^#Port 22/Port 4545/' /etc/ssh/sshd_config
              systemctl restart sshd
              EOF

  tags = {
    Name = var.instance_name
  }
}
```

```hcl
// elastic_ip.tf

resource "aws_eip" "ec2_eip" {
  vpc = true
}

resource "aws_eip_association" "eip_assoc" {
  instance_id   = aws_instance.ec2_instance.id
  allocation_id = aws_eip.ec2_eip.id
}
```

```hcl
// outputs.tf

output "private_key_pem" {
  value       = local_file.private_key_pem.content
  description = "The content of the private key."
  sensitive   = true
}

output "public_key_openssh" {
  value       = tls_private_key.ec2_private_key.public_key_openssh
  description = "The public key in OpenSSH format."
}
```

```hcl
// dev.tfvars

region        = "us-west-2"
ami           = "ami-0c55b159cbfafe1f0"
instance_type = "t2.micro"
subnet_id     = "subnet-0bb1c79de3EXAMPLE"
vpc_id        = "vpc-0bb1c79de3EXAMPLE"
security_group_name = "my-sec-group"
availability_zone   = "us-west-2a"
ebs_volume_size     = 20
ebs_volume_type     = "gp3"
instance_name       = "my-ec2-instance"
```
"""

# Split the code into blocks based on the marker
# blocks = terraform_code.strip().split("```hcl")
terraform_code=terraform_code.strip().split("```hcl")
output_folder="./project"
for block in terraform_code:
  if block:
    block=block.strip()
    file_name=block.splitlines()[0][3:]
    print(file_name)
    content =  "\n".join(block.splitlines()[1:]).strip('```')
   

    with open(os.path.join(output_folder, file_name), "w") as f:
      f.write(content + "\n")

print("Terraform files have been split and saved.")
