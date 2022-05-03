import json

# Here is a small change
# Another test
# Here is another small change to test something else out

def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps("Here we are from Github")
    }
