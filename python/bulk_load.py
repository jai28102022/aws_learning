import csv
import boto3

def load_csv():
    filename = "instances-demo.csv"
    file = open(filename)
    data = csv.DictReader(file, delimiter=',')
    for x1 in data:
        create_instance(x1.get("instance-name"), x1.get("instance-type"))
    file.close()

def create_instance(instance_name, instance_type,pkg):
    machine_name = instance_name
    if machine_name:
       ec2 = boto3.resource('ec2')
       userdata = """#!/bin/bash
yum update
apt install {0} -y"""
       imageid = 'ami-024c319d5d14b463e'
       instancetype = instance_type
       instance = ec2.create_instances(
                   ImageId=imageid,
                   MinCount=1,
                   MaxCount=1,
                   InstanceType=instancetype,
                   KeyName="jai",
                   UserData=userdata.format(pkg)
                   )
       for x1 in instance:
          x1.create_tags(Tags=[{"Key": "Name", "Value": machine_name}])
       print(">>>", machine_name)

load_csv()
