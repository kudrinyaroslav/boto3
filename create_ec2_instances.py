import boto3

my_user_data = ''

ec2 = boto3.client('ec2')
response = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'standard',
                'Encrypted': False
            },
        },
    ],
    ImageId='ami-0bd39c806c2335b95',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
    Placement={
        'AvailabilityZone': 'eu-central-1b',
        'Tenancy': 'default',
    },
    UserData= my_user_data,
    ClientToken='yaroslav-key-frankfurt',
    DisableApiTermination=False,
    DryRun=False,
    EbsOptimized=False,

    InstanceInitiatedShutdownBehavior='stop',
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeleteOnTermination': True,
            'DeviceIndex': 0,
            'Groups': [
                'sg-0bd9d92ecad8d71f0',
            ],
            'SubnetId': 'subnet-b5d607c9',
            'InterfaceType': 'interface',
            'NetworkCardIndex': 0
        },
    ],
)