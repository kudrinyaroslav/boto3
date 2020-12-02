import boto3
from botocore.exceptions import ClientError


efs = boto3.client('efs')

class efs_class:
    def __init__(self):
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
        self.fsi = response['FileSystemId']
        print('Created elastic file system with id=', self.fsi)
    def create_mount_target(self, si, vpcg):
        efs.create_mount_target(
                        FileSystemId=self.fsi,
                        SubnetId=si,
                        SecurityGroups=[
                            vpcg,
                        ]
                    )
        print('created mount tagret')
    def get_fsi(self):
        return self.fsi