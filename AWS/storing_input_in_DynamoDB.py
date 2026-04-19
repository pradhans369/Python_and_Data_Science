import boto3
from dotenv import load_dotenv
import os
import random

# loading the key and secret from env.test
load_dotenv("env.test")

# connecting the py to the DynamoDB and storing it in an obj
db = boto3.resource("dynamodb", region_name='ap-south-1')       # which putting dynamodb you have to write it in lowercase

# linking the db obj to a table and storing it in an obj
table =  db.Table('data_test')                                  # here you have to put the table name you have created in DynamoDB in AWS


def register():
    print("--- AWS DynamoDB User Registration ---")

    # getting user input
    name = input("ENTER FULL NAME : ").lower()                  # receiving the username in lowercase
    email = input("ENTER E-MAIL : ")
    password = input("ENTER PASSWORD : ")

    # generating 6 digit user id as there is also a feature call "id" in the data_test created in AWS which is a 'primary key'
    user_id = random.randint(100000, 999999)

    print(f"\n\nSAVING {name}'s USER DETAILS TO THE SERVER...\n\n")

    # saving to the database using try-catch
    try:
        table.put_item(
            Item={
                'id' : user_id,
                'name' : name,
                'email' : email,
                'password' : password
            }
        )

        print(f"✅ SUCCESS ! USER DETAILS SAVED.\n")

    except Exception as e:
        print(f"❌ Error: Something went wrong.")
        print(f"Technical details: {e}\n")



# -------------------------------------------------------------------------------------------------------------------------------

# calling the function
register()


