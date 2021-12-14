import json

from flask_restful import Api, Resource, reqparse
import  connect_table
from awscli.errorhandler import ClientError


table= connect_table.table1
cog = connect_table.cogclient
snsmsg = connect_table.snsclient

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
        
        # res = json.loads(json.dumps(response))

        # for i in range(0,len(res['UserAttributes'])):
        #     if(res['UserAttributes'][i]['Name']=="name") :
        #         nam = res['UserAttributes'][i]['Value']
        #     if(res['UserAttributes'][i]['Name']=="custom:mob_number"):
        #         mob = res['UserAttributes'][i]['Value']

        key={
            "userName": usr,
            "password": pwd
        }       
        upd={
            "token": accTo
        }

        table.update_item(Key=key, AttributeUpdates=upd)

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


def mobreg(mob):
    try:
        snsmsg.create_sms_sandbox_phone_number(
        PhoneNumber=mob,
        LanguageCode='en-US'
        )
        return {"success": "true"}
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}

        

