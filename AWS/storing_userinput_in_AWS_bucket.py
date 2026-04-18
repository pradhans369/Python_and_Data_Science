import boto3
import json
from dotenv import load_dotenv

# 1. This magically securely loads the hidden keys from your .env file
load_dotenv("env.test") 

# 2. You don't need to put ANY passwords here anymore!
# Boto3 will automatically check the environment variables in the background.
s3_client = boto3.client('s3') 

def save_to_s3(name, email):
    user_data = {
        "user_name": name,
        "user_email": email
    }
    json_string = json.dumps(user_data)
    
    s3_client.put_object(
        Bucket='ashura-bucket',            # put the bucket name
        # Key=f'{name}_data.json',              # creates a json file which stores the data
        Key=f'name_email/{name}_data.json',     # this will create a new folder and store all the data there
        Body=json_string                        # stores in string format
    )
    print(f"Success! {name}'s data was securely saved.")

# Run it!
save_to_s3("Lio Oberoy", "leo@outlook.com")
