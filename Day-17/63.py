import json

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):    
    return a*b

def div(a,b):
    return a/b  

def lambda_handler(event, context):
    a = event.get('a')
    b = event.get('b')
    operation = event.get('operation')
    
    if operation == 'sum':
        r = sum(a,b)
    elif operation == 'sub':
        r = sub(a,b)
    elif operation == 'mul':
        r =  mul(a,b)
    elif operation == 'div':
        r = div(a,b)
    else:
        return "Invalid operation"
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": r
        })
    }