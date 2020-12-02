import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

class sg_class:
    def __init__(self, vpc_id):
        response = ec2.create_security_group(GroupName='MySecurityGN', Description='MySecurityGN', VpcId=vpc_id)
        self.security_group_id = response['GroupId']
        data = ec2.authorize_security_group_ingress(
            GroupId=self.security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 2049,
                'ToPort': 2049,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort':3306,
                'ToPort': 3306,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ]
        )
        print('security group created ', self.security_group_id)
    def get_guid(self):
        return self.security_group_id


