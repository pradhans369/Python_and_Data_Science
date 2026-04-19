import boto3
from dotenv import load_dotenv
import os
import random

# 1. This loads your key ID and secret from the env.test file
load_dotenv("env.test")

# 2. Connect to DynamoDB in your specific region (Mumbai)
dynamodb = boto3.resource('dynamodb',region_name='ap-south-1')

table = dynamodb.Table('data_test')

def register_new_user():
    print("--- AWS DynamoDB User Registration ---")
    
    # taking input from the user
    name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    # IMPORTANT: Your table uses 'id' as a Number (N)
    # So we generate a random 6-digit number for the user ID
    user_id = random.randint(100000, 999999)

    print(f"\nSaving {name} to DynamoDB...")

    # 4. Save to the database
    try:
        table.put_item(
           Item={
                'id': user_id,           # Partition Key (Number)
                'user_name': name,
                'user_email': email,
                'user_password': password
            }
        )
        print(f"✅ Success! User saved perfectly.")
        print(f"Details saved: ID {user_id} | Email: {email}")
        
    except Exception as e:
        print(f"❌ Error: Something went wrong.")
        print(f"Technical details: {e}")

if __name__ == "__main__":
    register_new_user()
