import time
import boto3
from botocore.exceptions import ClientError



rds = boto3.client('rds')

class rds_class:
    def __init__(self, vpcg, vpc_id, si1, si2):
        self.response = rds.create_db_instance(
                    DBName='wordpress',
                    DBInstanceIdentifier='wordpress-inst',
                    AllocatedStorage=5,
                    DBInstanceClass='db.t2.micro',
                    Engine='mysql',
                    DBSubnetGroupName=self.create_db_subnet(si1, si2),
                    MasterUsername='admin',
                    MasterUserPassword='User1234',
                    VpcSecurityGroupIds=[
                        vpcg,
                    ]
                )
    def create_db_subnet(self, si1, si2):
        subnet = boto3.client('rds')
        response = subnet.create_db_subnet_group(
            DBSubnetGroupName='sample-subnet-group',
            DBSubnetGroupDescription='sample-subnet-group123',
            SubnetIds=[
                si1,
                si2
            ])
        return response['DBSubnetGroup']['DBSubnetGroupName']
    def get_ep(self):
        response = rds.describe_db_instances()
        return response['DBInstances'][0]['Endpoint']['Address']