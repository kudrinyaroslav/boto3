import boto3
from botocore.exceptions import ClientError



rds = boto3.client('rds')



response = rds.create_db_instance(
    DBName='wordpress',
    DBInstanceIdentifier='wordpress-inst',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='User1234',
    VpcSecurityGroupIds=[
        'sg-0bd9d92ecad8d71f0',
    ],
    BackupRetentionPeriod=0,
    Port=3306,
    MultiAZ=False,
    EngineVersion='8.0.20',
    AutoMinorVersionUpgrade=True,
    PubliclyAccessible=False,
    Tags=[
        {
            'Key': 'db_name',
            'Value': 'wordpress'
        },
    ],
    StorageType='standard',
    StorageEncrypted=False,
    CopyTagsToSnapshot=False,
    DeletionProtection=False,
)