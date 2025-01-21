choose_prompt="""

    Think like you are a expert in generating Terraform code for the cloud resources

    Choose the required prompts for the use case:  
        - ec2_prompt
        - relational_database_prompt
        - s3_bucket_prompt
    
    Give the response as a json, follow the below format
    Only choose the prompts from the specified prompts, dont use include any other prompt which are not mentioned
    
    {
    "required_prompts": [
        "ec2_prompt",...etc
         
        ]
    }
    Dont include any explanation or coding
    Only give the json format as mentioned

"""