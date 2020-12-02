import boto3
ec2 = boto3.client('ec2')

class ec2_class:
    def __init__(self, vpcg, si, ud):
        # создаем новый ec2 instance
        self.response = ec2.run_instances(InstanceType="t2.micro", 
                         MaxCount=1, 
                         MinCount=1, 
                         ImageId="ami-0bd39c806c2335b95",
                         UserData=ud,
                         NetworkInterfaces=[
                             {'AssociatePublicIpAddress': True, 
                              'DeviceIndex': 0,
                              'SubnetId': si,
                              'Groups': [vpcg],
                              }],
                         )
    def GetEc2Id(self):
        return self.response['Instances'][0]['InstanceId']
    