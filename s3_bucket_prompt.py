s3_bucket_prompt="""
    Generate Terraform code for an S3 bucket with the following requirements:
        1. The bucket must include tag of the bucket name .
        2. The ACL (Access Control List) should be configurable via a variable.
        3. Enable versioning for the bucket:
        - Use the `aws_s3_bucket_versioning` resource.
        - Make the `status` field (e.g., "Enabled", "Disabled") configurable via a variable.
        4. The bucket name should also be configurable via a variable.
"""