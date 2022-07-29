import boto3
client=boto3.client('ce')
response = client.get_cost_and_usage(
    TimePeriod={
                  ##Year-Month-Date
        'Start': '2022-07-10',
        'End': '2022-07-11'
    },
    Granularity='DAILY',
    Metrics=['BlendedCost']
    )
print(response)