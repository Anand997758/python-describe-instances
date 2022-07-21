import boto3
regions=[]
ec2=boto3.client('ec2')
client = ec2.describe_regions()
for i in client['Regions']:
    regions.append(i['RegionName'])
print(regions)
for y in range(len(regions)):
        
    client=boto3.client('autoscaling',region_name=regions[y])
    resource=client.describe_auto_scaling_groups()
    for x in resource['AutoScalingGroups']:

        a = client.describe_auto_scaling_groups(
            AutoScalingGroupNames=[x['AutoScalingGroupName']])
        for y in a['AutoScalingGroups']:
            print("GroupName=",
            y['AutoScalingGroupName'],
            "MinSize=",
            y['MinSize'],
            "MaxSize=",
            y['MaxSize'])