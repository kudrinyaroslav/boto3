import time

from class_create_vpc import VpcClass
from class_create_db import rds_class
from class_create_ec2 import ec2_class
from class_create_efs import efs_class
from class_create_elb import elb_class
from class_create_security_group import sg_class


# создаем vpc
vpc_inst = VpcClass()
vpc_id = vpc_inst.get_vpc_id()
vpc_inst.attach_to_ig()

# создаем subnets
si1 = vpc_inst.create_subnet('10.0.1.0/24', 'eu-central-1b')
si2 = vpc_inst.create_subnet('10.0.2.0/24', 'eu-central-1a')

# создаем группу безопасности и guid
sg_inst = sg_class(vpc_id)
sg_id = sg_inst.get_guid()

# создаем базу данных
rds_inst = rds_class(sg_id, vpc_id, si1, si2)

# cоздаем файловую систему
efs_inst = efs_class()

# создаем ec2
vm1 = ec2_class(sg_id,si1)
vm1id = vm1.GetEc2Id()
vm2 = ec2_class(sg_id, si2)
vm2id = vm2.GetEc2Id()


# создаем load balancer
elb_inst = elb_class('myload', si1, si2, sg_id)
elb_inst.register_inst_wit_load_balancer(vm1id, vm2id)

time.sleep(50)

# прикрепляем к файловой системе группу безопасности и подсеть
efs_inst.create_mount_target(si1, sg_id)
efs_inst.create_mount_target(si2, sg_id)
