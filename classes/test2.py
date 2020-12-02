import boto3
client = boto3.client('rds')
response = client.describe_db_instances()
print(response['DBInstances'][0]['Endpoint']['Address'])