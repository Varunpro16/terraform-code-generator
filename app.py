import autogen
import os
import re

base_path = "./"

def start_app():
    # Load the configuration list from a JSON file, filtering for specific models
    config_list = autogen.config_list_from_json(
        os.path.join(base_path, "OAI_CONFIG_LIST.json"),
        filter_dict={"model": ["gpt-4o"]},
    )
    
    assistant = autogen.ConversableAgent(
        name="Terraform_Code_Generator_Agent",
        system_message="Assist with generating Terraform code for various AWS cloud infrastructure setups.",
        llm_config={"config_list": config_list},
    )

    # Proxy Agent for auto execution
    user_proxy = autogen.ConversableAgent(
        name="User_Proxy",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )

    user_prompt = userinput+'''

        - Elastic IP association and creation.
        - A TLS private key generation and saving it to a local file.
        - Creation of an AWS Key Pair using the generated TLS private key.
        - Security Group configuration to allow SSH, HTTP, and HTTPS traffic.
        - EC2 Instance setup with the specified AMI, instance type, and security group.
        - Volume configuration (EBS) for the EC2 instance with specific size and type (gp3).
        - User data script to change the SSH port from 22 to 4545.
        - Output sensitive details such as the private key content and public key.
        - Variables for region, subnet, VPC, instance details, and security group name.
        - Subnet ID and availability zone filters for the subnet.

        Make sure to structure the code with the following specifications:

        - Use `aws_eip_association` to associate the elastic IP.
        - Use `aws_eip` to create an Elastic IP.
        - Use `tls_private_key` for generating the private key.
        - Use `aws_key_pair` for creating the key pair.
        - Use `aws_security_group` for the security group setup.
        - Use `aws_instance` for EC2 instance creation with a user-data script that modifies SSH configuration.
        - When referencing a security group for the EC2 instance, use the `vpc_security_group_ids` attribute and provide the security group ID, not the name.
        - Do not use the `security_groups` attribute with the name of the security group.

        Ensure the private key is saved to a local file with restricted permissions.
        Include output blocks for the private key and public key.

        **Important:** Avoid Duplicate Resource Names Across Terraform Files:
        - Give different names for the AWS resources involved in this project.
        - Use appropriate variables for region, instance type, subnet ID, VPC ID, and other parameters.
        - When splitting and organizing Terraform resources into separate files, ensure that resource names are unique and do not repeat across different files.
        - Each resource type (e.g., `tls_private_key`, `aws_key_pair`, `local_file`, `aws_security_group`, `aws_instance`, `aws_eip`, `aws_eip_association`) should use a unique identifier to avoid conflicts when referenced in other parts of the Terraform code.

        **File Organization:**
        1. **provider.tf:** Contains the provider configuration for AWS.
        2. **variables.tf:** Defines all the variables used across the resources, without any default value.
        3. **key_pair.tf:** Manages the TLS private key generation and AWS key pair resources.
        4. **security_group.tf:** Contains the configuration for the security group.
        5. **ec2.tf:** Defines the EC2 instance resource and its associated configurations.
        6. **elastic_ip.tf:** Manages the Elastic IP and its association with the EC2 instance.
        7. **outputs.tf:** Outputs the sensitive data such as private keys and public keys.
        8. **dev.tfvars:** Write respective `.tfvars` specifications based on `variables.tf`. Maintain correct names as specified in the `variables.tf`.

        Ensure the files are linked properly using variable references and outputs, maintaining modularity and readability.

        Output example is mentioned below for each module:

        ```hcl
        // provider.tf

        terraform {
            required_providers {
                aws = {
                source  = "hashicorp/aws"
                version = "~> 4.0"
                }
            }
            required_version = ">= 1.0.0"
        }

        provider "aws" {
            region = var.region
        }
        '''

    # Start the chat with the assistant
    chat = user_proxy.initiate_chat(assistant, message=user_prompt,max_turns=1)

    # Extract the generated Terraform code from the last chat message
    terraform_code = chat.chat_history[-1]['content'] if chat.chat_history else "No Terraform code generated."

    
    blocks = terraform_code.strip().split("###")
    del blocks[0]

    output_folder="./project"
    for block in blocks:
        if block.strip():
            # Extract file name and content
            lines = block.strip().split("\n", 1)
            file_name = lines[0].strip()
            content = lines[1] if len(lines) > 1 else ""
            content=content.strip("```").replace("hcl\n", "").strip("```")
            file_name=file_name[3:]
            print(file_name.endswith(".tf"))
            if not file_name.endswith(".tf") and not file_name.endswith(".tfvars"):
                continue
            with open(os.path.join(output_folder, file_name), "w") as f:
                f.write(content + "\n")


# Start the application
start_app()
