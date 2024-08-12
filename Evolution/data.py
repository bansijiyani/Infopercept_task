import json
import boto3

def lambda_handler(event , context):
    try:
        db = boto3.resource('dynamodb')
        table = db.Table('marksheet')

        res = table.scan()

        data = res.get('Items')
        return data
    except Exception as e:
        return (e)
    