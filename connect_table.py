import boto3

# dynamoDB = boto3.resource("dynamodb", aws_access_key_id="ASIAT7IRXYX5PS6NRLR3",
#                           aws_secret_access_key="M2rzYhdoiiD35iKw6S731uUBfj9nX8hnFl/FrkNR",
#                           aws_session_token="FwoGZXIvYXdzEJv//////////wEaDOZybOnn0RN28I27WiLKASAn96epkigmr3dwI7VX7/Oal62VR26AxoIUpMCHcAPQ5lKJc7pWRJmFmmMTRnBqHeWq+/JcGFS4Nz8bC2nrKVmjHqq6MnIiyz8+kbOelK9HCwq5p4FboE+WUu/5xK66987zIKtQs/wgxySo2is7dzuBg7RGU8QHkyYPfWfsVDUkQdG+GhWJfW2GwF/0+eulweRyC+LiN3oP1DUdp5M9yQqew01RRpDJCveGjS6moOxERGvo+Oq7pMfM0FWWjYZln8S8UElIzfSeLaMovcGujQYyLUGmaeVc6oyUGHIPjasudRlKBzdnUrCDn006XFmzwiOj0CNXycdHAySVkNltKQ==")

dynamoDB = boto3.resource("dynamodb", region_name='us-east-1')



# dynamoDB = boto3.resource("dynamodb", region_name='us-east-1')



table1 = dynamoDB.Table('userTable')
table2 = dynamoDB.Table('recipeTable')
