import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
	bucket ='lambdapocs3put'

	transactionToUpload = {}
	transactionToUpload['transactionId'] = '12345'
	transactionToUpload['type'] = 'PURCHASE'
	transactionToUpload['amount'] = 20
	transactionToUpload['customerId'] = 'CID-11111'

	fileName = 'CID-12' + '.json'

	uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Put Complete')
