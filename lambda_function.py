import json

# Here is a small change

def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps("Here we are from Github")
    }
