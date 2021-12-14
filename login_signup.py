import json

from flask_restful import Api, Resource, reqparse
import  connect_table
from awscli.errorhandler import ClientError


table= connect_table.table1
cog = connect_table.cogclient
COGNITO_USER_CLIENT_ID = "riiugb6k7m01m734ctvt420vv"

# Login Block
def login(usr, pwd):
    try:
        # response = table.get_item(
        #     Key={
        #         "userName": usr,
        #         "password": pwd

        #     }
        # )

        response = cog.initiate_auth(
        ClientId=COGNITO_USER_CLIENT_ID,
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={"USERNAME": usr, "PASSWORD": pwd},
        )
        accTo = response["AuthenticationResult"]["AccessToken"]
        response = cog.get_user(AccessToken=accTo)
        res = json.loads(json.dumps(response))
        # print(res['Username'])
        # for i in range(0,len(res['UserAttributes'])):
        #     if(res['UserAttributes'][i]['Name']=="phone_number" or res['UserAttributes'][i]['Name']=="name"):
        #         print(res['UserAttributes'][i]['Value'])

        return json.loads(json.dumps(response))
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

        
        cog.sign_up(
            ClientId=COGNITO_USER_CLIENT_ID,
            Username=usr,
            Password=pwd,
            UserAttributes=[{"Name": "name", "Value": name},{"Name":"custom:mob_number","Value":mob}],
        )

        return {"success": "true"}
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}

        

