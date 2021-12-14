import json

from flask_restful import Api, Resource, reqparse
import  connect_table
from awscli.errorhandler import ClientError


table= connect_table.table1


# Login Block
def login(usr, pwd):
    try:
        response = table.get_item(
            Key={
                "userName": usr,
                "password": pwd

            }
        )
        return json.loads(json.dumps(response['Item'], indent=4))
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}



def signUp(usr,pwd,name,mob):
    try:
        table.put_item(Item={
            "userName": usr,
            "name": name,
            "mob_number": mob,
            "password": pwd,
        })
        return {"success": "true"}
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}

        

