import boto3
import csv
regions=[]
ec2=boto3.client('ec2')
client = ec2.describe_regions()
for i in client['Regions']:
    regions.append(i['RegionName'])
print(regions)
fo=open("ec2_qwer.csv",'w',newline='')
data_obj=csv.writer(fo)
for each_region in regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_region)
data_obj.writerow(['sno','instance_id','instance_type','key_name','public_ip_address','private_ip_address'])   