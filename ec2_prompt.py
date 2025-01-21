ec2_prompt='''

    Things need to know while creating EC2 using Terraform
    
        - Elastic IP association and creation.
        - A TLS private key generation and saving it to a local file.
        - Creation of an AWS Key Pair using the generated TLS private key.
        - Security Group configuration to allow SSH, HTTP, and HTTPS traffic.
        - EC2 Instance setup with the specified AMI, instance type, and security group.
        - Volume configuration (EBS) for the EC2 instance with specific size and type (gp3).
        - Include root volume in the aws_instance and mention volume_type, volume_size, delete_on_termination. Put the values for these variables in dev.tfvars file
        - Output sensitive details such as the private key content and public key.
        - Variables for region, subnet, VPC, instance details, and security group name.

        Ensure the private key is saved to a local file with restricted permissions.
        Example:
            resource "local_file" "private_key" {
                filename       = "private_key_pair.pem" 
                content        = tls_private_key.key_pair.private_key_pem
                file_permission = "0600" 
            }
        Include output blocks for the private key and public key.

        Use appropriate variables for region, instance type, subnet ID, VPC ID, and other parameters.
        Each resource type (e.g., `tls_private_key`, `aws_key_pair`, `local_file`, `aws_security_group`, `aws_instance`, `aws_eip`, `aws_eip_association`) should use a unique identifier to avoid conflicts when referenced in other parts of the Terraform code.

        '''