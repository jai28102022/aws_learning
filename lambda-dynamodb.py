import json
import boto3 

def lambda_handler(event, context):
    print("event>> ", event)
    print("context>>>", context)
    req_method = event.get("httpMethod", "GET")
    req_resource = event.get("resource", '/')
    req_path = event.get("path", '/')
    req_body = event.get("body", '')
    if req_method == 'POST':
        return user_create(req_body)
    elif req_method == 'DELETE':
        return user_del(req_body)
    elif req_method == 'PATCH':
        return user_update(req_body)
    else: 
        return user_list()
    

def user_create(req_body):
    client = boto3.resource('dynamodb', region_name='ap-south-1')
    user = client.Table('user')
    user_dict = json.loads(req_body)
    user.put_item(Item=user_dict)
    return {
        'statusCode': 200,
        'body': user_dict.get("userid")
    }

def user_list():
    client = boto3.resource('dynamodb', region_name='ap-south-1')
    user = client.Table('user')
    return {
        'statusCode': 200,
        'body': json.dumps(user.scan())
    }

def user_del(req_body):
    client = boto3.resource('dynamodb', region_name='ap-south-1')
    user = client.Table('user')
    user_dict = json.loads(req_body)
    user.delete_item(Key={ 'userid': user_dict.get('userid')})
    return {
        'statusCode': 200,
        'body': json.dumps('Del user!')
    } 

def user_update(req_body):
    client = boto3.resource('dynamodb', region_name='ap-south-1') 
    user = client.Table('user')
    user_dict = json.loads(req_body)  
    user.put_item(Item=user_dict) 
    return {
        'statusCode': 200,
        'body': user_dict.get("userid") 
    }
