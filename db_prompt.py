relational_database_prompt=''' 
    The prompt for this Terraform setup involves the following key tasks:

    - AWS Provider Configuration: Use the `provider` block to specify the AWS region for the resources.
    - Security Group for RDS: Define a security group that allows inbound traffic on port 5432 (PostgreSQL), with a rule that allows traffic from all sources (`0.0.0.0/0`). This rule should be restricted in a production environment.
    - RDS Subnet Group: Create a subnet group for the RDS instance using the provided subnet IDs to ensure the RDS instance is placed in the desired subnets.
    - RDS Instance Creation: Create an Amazon RDS PostgreSQL instance with specific configurations, such as storage size, instance class, database name, master username, and password. Use the security group and subnet group created earlier. Ensure the instance is publicly accessible (set to `true` or `false` as needed).
    - File Organization: 
    - `provider.tf`: Contains the provider setup for AWS.
    - `variables.tf`: Defines variables like region, subnet IDs, and database credentials.
    - `security_group.tf`: Defines the security group for the RDS instance.
    - `db_subnet_group.tf`: Configures the RDS subnet group.
    - `db_instance.tf`: Defines the RDS instance with all configurations.
    - `outputs.tf`: Contains output blocks to expose the RDS instance's endpoint and port.
    - `dev.tfvars`: Specifies values for the variables used in the Terraform configuration.

    In this Terraform configuration, variables have been defined for the following parameters to increase flexibility and configurability:

    - allocated_storage: Specifies the initial allocated storage size for the RDS instance (in GB).
    - max_allocated_storage: Defines the maximum storage size for the RDS instance, allowing auto-scaling of storage.
    - storage_type: Specifies the storage type for the RDS instance, such as `gp2` (General Purpose SSD), with a default value.
    - engine: Defines the database engine to be used for the RDS instance, such as PostgreSQL, with a default value.
    - engine_version: Specifies the version of the database engine (e.g., version 13 for PostgreSQL).
    - instance_class: Sets the instance class (e.g., `db.t3.micro`) for the RDS instance, determining the CPU, memory, and network performance.
    - db_name: Sets the initial database name that will be created in the RDS instance.
    - username: The master username for the RDS instance.
    - password: The master password for the RDS instance.
    - publicly_accessible: Defines whether the RDS instance is publicly accessible from the internet (set to `true` or `false`).
    - skip_final_snapshot: Specifies whether to skip the final snapshot when deleting the RDS instance (set to `true` or `false`).
    These variables should be present in `variables.tf` file and dev.tfvars file, allowing values to be customized via a `dev.tfvars` file, thus ensuring modular and reusable Terraform code.
    Put dummy values in dev.tfvars file
    
    Variables should present in dev.tfvars:
    allocated_storage, max_allocated_storage, storage_type, engine,engine_version, instance_class, db_name, username, password, publicly_accessible, skip_final_snapshot


    Make sure the variables are properly declared in `variables.tf` and values are provided in `dev.tfvars`. This approach ensures modularity and allows for easier management of infrastructure.
    Do not mention any paragraph or line to explain the code
        Output example is mentioned below for each module:  - provide the file name inside the code block itself

        ```hcl
        // provider.tf (this is the file name)

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