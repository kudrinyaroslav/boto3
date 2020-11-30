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
    #AvailabilityZone='eu-central-1',
    #DBSubnetGroupName='string',
    #PreferredMaintenanceWindow='string',
    #DBParameterGroupName='string',
    BackupRetentionPeriod=0,
    #PreferredBackupWindow='string',
    Port=3306,
    MultiAZ=False,
    EngineVersion='8.0.20',
    AutoMinorVersionUpgrade=True,
    #LicenseModel='string',
    #Iops=123,
    #OptionGroupName='string',
    #CharacterSetName='string',
    #NcharCharacterSetName='string',
    PubliclyAccessible=False,
    Tags=[
        {
            'Key': 'db_name',
            'Value': 'wordpress'
        },
    ],
    #DBClusterIdentifier='string',
    StorageType='standard',
    #TdeCredentialArn='string',
    #TdeCredentialPassword='string',
    StorageEncrypted=False,
    #KmsKeyId='string',
    #Domain='string',
    CopyTagsToSnapshot=False,
    #MonitoringInterval=123,
    #MonitoringRoleArn='string',
    #DomainIAMRoleName='string',
    #PromotionTier=123,
    #Timezone='string',
    #EnableIAMDatabaseAuthentication=True|False,
    #EnablePerformanceInsights=True|False,
    #PerformanceInsightsKMSKeyId='string',
    #PerformanceInsightsRetentionPeriod=123,
    #EnableCloudwatchLogsExports=[
    #    'string',
    #],
    #ProcessorFeatures=[
    #    {
    #        'Name': 'string',
    #        'Value': 'string'
    #    },
    #],
    DeletionProtection=False,
    #MaxAllocatedStorage=123
)