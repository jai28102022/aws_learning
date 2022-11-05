import boto3

client = boto3.client('ec2')

response = client.describe_instances()

for x1 in response:
  print(x1)
