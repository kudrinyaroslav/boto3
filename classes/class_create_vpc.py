import boto3



class VpcClass:
    def __init__(self):
        self.vpc = boto3.client('ec2')
        response = self.vpc.create_vpc(
            CidrBlock='10.0.0.0/16',
            InstanceTenancy='default',
        )
        self.vpc_id = response['Vpc']['VpcId']
        print('vpc created ', self.vpc_id)
    def create_subnet(self, cb, az):
        response = self.vpc.create_subnet(
                CidrBlock=cb,
                VpcId=self.vpc_id,
                AvailabilityZone=az,
        )
        s_id = response['Subnet']['SubnetId']
        print('subnet created ', s_id)
        return s_id
    def attach_to_ig(self):
        ig_id = self.vpc.create_internet_gateway()['InternetGateway']['InternetGatewayId']
        self.vpc.attach_internet_gateway(InternetGatewayId=ig_id,
                                         VpcId=self.vpc_id)
        print('VPC attached to internet gateway')
    def get_vpc_id(self):
        return self.vpc_id

    
