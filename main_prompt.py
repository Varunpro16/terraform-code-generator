main_prompt = """

        ## Code Structure Specifications
        - Specify resource types needed for your use case (e.g., `aws_instance`, `aws_s3_bucket`)
        - Detail required attributes or settings for each resource
        - List any dependencies or references between resources
        - Specify any naming conventions or unique identifier requirements
        - Include any specific resource association methods

        ## Base File Structure
        1. provider.tf: Provider configuration
        2. variables.tf: Variable definitions without default values
        3. outputs.tf: Output definitions
        4. dev.tfvars: Environment-specific variable values. 

        Do not include any tags in dev.tfvars file
        Do not include any tags in variables.tf file

        ## Optional Module Files (Include if needed based on the use case)
        Based on your use case, include only the relevant files:
        - security.tf: For security groups, IAM roles, policies
        - vpc.tf: For vpc configurations
        - ec2.tf: For ec2 instances configurations
        - key_pair.tf: For aws_key_pair and tls_private_key configurations
        - elastic_ip.tf For aws_eip and aws_eip_association configurations
        - load_balancer.tf: For elastic load balancer related configurations
        - subnets.tf: For subnet configurations
        - rds.tf: For Relational database configurations
        - route_table.tf: For route table configurations
        - db_subnet_group.tf: Configures the RDS subnet group.
        - db_instance.tf: Defines the RDS instance with all configurations.
        - user_pool.tf: Defines the user pool 
        - identity_pool.tf: Defines the identity pool 
        - s3_bucket.tf: For S3 bucket configurations
        - dynamodb.tf: For DynamoDB configurations
        - monitoring.tf: For CloudWatch, SNS configurations
        - cdn.tf: For CloudFront configurations
        - dns.tf: For Route53 configurations

"""

