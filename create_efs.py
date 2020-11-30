import boto3
from botocore.exceptions import ClientError

efs = boto3.client('efs')

response = efs.create_file_system(
    PerformanceMode='generalPurpose',
    Encrypted=False,
    Tags=[
        {
            'Key': 'name',
            'Value': 'MyEFS'
        },
    ]
)

response = efs.create_mount_target(
    FileSystemId='fs-5eca8106',
    SubnetId='subnet-b5d607c9',
    SecurityGroups=[
        'sg-0bd9d92ecad8d71f0',
    ]
)

response = efs.create_mount_target(
    FileSystemId='fs-5eca8106',
    SubnetId='subnet-81ff65eb',
    SecurityGroups=[
        'sg-0bd9d92ecad8d71f0',
    ]
)
response = efs.create_mount_target(
    FileSystemId='fs-5eca8106',
    SubnetId='subnet-59812515',
    SecurityGroups=[
        'sg-0bd9d92ecad8d71f0',
    ]
)
