import json
import boto3


def create_response(status_code, message):
    try:
        return {
            "headers": {
                "Content-Type": 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({
                'statusCode': status_code,
                'message': message,
            })
        }
    except Exception as e:
        print(e)
        return ("Error")
    

def lambda_handler(event , context):

    try:
        db = boto3.resource('dynamodb')
        table = db.Table('marksheet')
        
        body = json.loads(event['body'])
        
        print(event)

        id = body.get('id')
        name = body.get('name')
        sem = body.get('sem')
        c_name = body.get('c_name')
        
        m1 = body.get('m1')
        m2 = body.get('m2')
        m3 = body.get('m3')
        m4 = body.get('m4')
        total_marks = m1 + m2 + m3 + m4
        per = total_marks / 4 

        table.put_item(

            Item = {
                id : id,
                name : name,
                sem : sem,
                c_name : c_name,
                total_marks : total_marks,
                per : per  
            } 
        )

        return create_response(200,"Error")
        
    except Exception as e:
        print(e)
        return create_response(200,"Error")