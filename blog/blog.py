import json
import os
import boto3
import time

db = boto3.client('dynamodb')
TABLE_NAME = os.getenv('ENTRY_TABLE')

def get_entry(event, context):
    print(event)
    key = {
        'id':{'N': str(event['pathParameters']['id'])}
    }
    entry = db.get_item(TableName=TABLE_NAME, Key=key)
    response = {
        "statusCode": 200,
        "body": json.dumps(entry)
    }
    return response

def get_entries(event, context):
    items = db.scan(TableName=TABLE_NAME)['Items']
    response = {
        "statusCode": 200,
        "body": json.dumps(items)
    }

    return response

def create_entry(event, context):
    body = json.loads(event['body'])
    entry = {
        'id': {'N':str(time.time())},
        'created_date':{'S':body['date']},
        'tags': {'SS': body['tags']},
        'body':{'S': body['body']}
    }
    put = db.put_item(TableName=TABLE_NAME,Item=entry)
    response = {
        "statusCode": 201,
        "body": json.dumps(put)
    }

    return response

def update_entry(event,context):
    key = {
        'id':{'N': str(event['pathParameters']['id'])}
    }
    
def delete_entry(event, context):
    key = {
        'id':{'N': str(event['pathParameters']['id'])}
    }
    delete = db.delete_entry(TableName=TABLE_NAME, Key=key)
    response = {
        "statusCode": 200,
        "body": json.dumps(delete)
    }
    return response


