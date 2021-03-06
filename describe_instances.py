import boto3
client = boto3.client('ec2',region_name="us-east-1")
sns = boto3.client('sns',region_name="us-east-1")
response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'Dev',
            ]
        },
    ]
)
a = response['Reservations']
for x in a:
    b = x['Instances'][0]['InstanceId']
    c = x['Instances'][0]['State']['Name']
    # print(d)
    res = client.stop_instances(
        InstanceIds=[b]
    )
    f = res['StoppingInstances'][0]['CurrentState']['Name']
    e = res['StoppingInstances'][0]['PreviousState']['Name']
    g = res['StoppingInstances'][0]['InstanceId']
    h = "instance id is {}, its previos state is {} andits current satate is {}".format(g,e,f)
    print(h)
    res1 = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:115935572748:Production_alerts',
        Message=h,
        Subject='PRO-ALERTS'
    )
