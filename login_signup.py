import json

from flask_restful import Api, Resource, reqparse
import  connect_table
from awscli.errorhandler import ClientError


table= connect_table.table1
cog = connect_table.cogclient

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
        # table.put_item(Item={
        #     "userName": usr,
        #     "password": pwd,
        #     "name": name,
        #     "mob_number": mob,
        # })

        COGNITO_USER_CLIENT_ID = "722d9o00ns6alnb92n37g1imh5"
        cog.sign_up(
            ClientId=COGNITO_USER_CLIENT_ID,
            Username=usr,
            Password=pwd,
            UserAttributes=[{"Name": "name", "Value": name},{"Name":"phone_number","Value":mob}],
        )

        return {"success": "true"}
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}

        

