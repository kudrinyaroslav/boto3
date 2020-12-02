import boto3
from botocore.exceptions import ClientError

elb = boto3.client('elb')


class elb_class:
    def __init__(self, lbn, si1, si2, vpcg):
        self.lbn = lbn
        elb.create_load_balancer(
                    LoadBalancerName=self.lbn,
                    Listeners=[
                        {
                            'Protocol': 'HTTP',
                            'LoadBalancerPort': 80,
                            'InstanceProtocol': 'HTTP',
                            'InstancePort': 80,
                        },
                    ],
                    Subnets=[
                        si1,
                        si2
                    ],
                    SecurityGroups=[
                        vpcg,
                    ],
                    Scheme='internet-facing',
                    Tags=[
                        {
                            'Key': 'name',
                            'Value': 'load'
                        },
                    ]
                )
        print('load balancer created ', self.lbn)
    def register_inst_wit_load_balancer(self, inst1, inst2):
        elb.register_instances_with_load_balancer(
                    LoadBalancerName=self.lbn,
                    Instances=[
                        {
                            'InstanceId': inst1
                        },
                        {
                            'InstanceId': inst2
                        },
                    ]
                )