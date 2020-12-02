import boto3
from botocore.exceptions import ClientError

elb = boto3.client('elb')

response = elb.create_load_balancer(
    LoadBalancerName='Myelb',
    Listeners=[
        {
            'Protocol': 'HTTP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'HTTP',
            'InstancePort': 80,
        },
    ],
    Subnets=[
        'subnet-b5d607c9',
        'subnet-81ff65eb',
        'subnet-59812515'
    ],
    SecurityGroups=[
        'sg-0bd9d92ecad8d71f0',
    ],
    Scheme='internet-facing',
    Tags=[
        {
            'Key': 'name',
            'Value': 'load'
        },
    ]
)

response = client.register_instances_with_load_balancer(
    LoadBalancerName='Myelb',
    Instances=[
        {
            'InstanceId': 'string'
        },
        {
            'InstanceId': 'string'
        },
    ]
)