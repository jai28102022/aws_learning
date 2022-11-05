import boto3

client = boto3.client('ec2')

response = client.describe_instances()

for x1 in response["Reservations"]:
  print(">>> ", x1["Instances"][0].get("Tags","NA"))
  print(x1["Instances"][0]["State"])
