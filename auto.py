import boto3
import csv
regions=[]
ec2=boto3.client('ec2')
client = ec2.describe_regions()
for i in client['Regions']:
    regions.append(i['RegionName'])
print(regions)
for y in range(len(regions)):
        
    client=boto3.client('autoscaling',region_name=regions[y])
    resource=client.describe_auto_scaling_groups()
    for x in resource['AutoScaling']:

        a = client.describe_auto_scaling_groups(
            AutoScalingGroupNames=[x['AutoScalingGroupName']])
        for y in a['AutoScalingGroups']:
            print("GroupName=",y['AutoScalingGroupName'],"MinSize=",y['MinSize'],"MaxSize=",y['MaxSize'])


#writing into a file
fo=open("ec2_qwer.csv",'w',newline='')
data_obj=csv.writer(fo)
data_obj.writerow(['sno','instance_id','instance_type','key_name','public_ip_address','private_ip_address'])
#data_obj.writerow(["s3_buckets"])


cnt=1
for each_region in regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_region)
    for each_ins_in_reg in ec2_re.instances.all():
        data_obj.writerow([cnt,each_ins_in_reg.instance_id,each_ins_in_reg.instance_type,each_ins_in_reg.key_name,each_ins_in_reg.public_ip_address,each_ins_in_reg.private_ip_address])
        #data_obj.writerow([bucket.name])
        #print([cnt,each_ins_in_reg.instance_id,each_ins_in_reg.instance_type,each_ins_in_reg.key_name,each_ins_in_reg.public_ip_address,each_ins_in_reg.private_ip_address])
        cnt+=1