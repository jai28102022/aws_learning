import boto3
import sys

client = boto3.client('ec2')

response = client.describe_instances()


print("InstanceID\t\tState\t\tTags")
print("-"*60)
for x1 in response["Reservations"]:
  instance_id = x1["Instances"][0]["InstanceId"]
  state = x1["Instances"][0]["State"]["Name"]
  tags = "NA"
  if x1["Instances"][0].get("Tags"):
      tags = ""
      for tag in x1["Instances"][0].get("Tags"):
         tags += tag["Key"]+": "+tag["Value"] + ", "
  print(instance_id, "\t", state, "\t", tags)

ec2 = boto3.resource('ec2')
machine_id = input("Enter you machine id: ")
if machine_id:
    ec2.instances.filter(InstanceIds=[machine_id,]).terminate()

#machine_name = input("Enter you machine name: ")
#if machine_name:
#    ec2 = boto3.resource('ec2')
#    imageid = 'ami-024c319d5d14b463e'
#    instancetype = 't2.micro'
#    instance = ec2.create_instances(
#                ImageId=imageid,
#                MinCount=1,
#                MaxCount=1,
#                InstanceType=instancetype,
#                KeyName="jai" )
#    for x1 in instance:
#       x1.create_tags(Tags=[{"Key": "Name", "Value": machine_name}])
