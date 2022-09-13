import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket ='lambdapocbckettoreceivedatafroms3put'
    transactionToUpload = {}
    transactionToUpload['id'] = event['id']
    transactionToUpload['name'] = event['name']
    transactionToUpload['email'] = event['email']
    fileName = event['id'] + '.json'
    uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))
    s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)
    print('Put Complete')
    return {'r':'Done'}
