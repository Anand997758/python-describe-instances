import boto3
client = boto3.client('ec2', region_name='ap-southeast-2')

ec2_region = [region['RegionName'] for region in client.describe_regions()['Regions']]

for regions in ec2_region:
    conn = boto3.resource('ec2', region_name=regions)
    instances = conn.instances.filter()
    for instance in instances:
        if instance.state["Name"] == "running":
            print (instance.id, instance.instance_type, regions)