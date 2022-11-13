--------------------------------------
OS: Ubuntu 20.04 LTS 
--------------------------------------

mkdir your_name 
sudo apt update
sudo apt install awscli
sudo apt install  python3-boto3
aws configure        

cd ~/your_name 
wget https://raw.githubusercontent.com/jai28102022/aws_learning/main/python/vm_list.py
cat test.py 
python3 test.py 


cd ~/your_name 
wget https://raw.githubusercontent.com/jai28102022/aws_learning/main/python/bulk_load.py
wget https://raw.githubusercontent.com/jai28102022/aws_learning/main/python/instances-demo.csv
cat bulk_load.py
cat instances-demo.csv
python3 bulk_load.py 



