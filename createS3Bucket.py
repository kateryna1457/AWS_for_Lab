import os
import boto3
from botocore.exceptions import ClientError

ACCESS_KEY = 'AWS_ACCESS_KEY_ID'
SECRET_KEY = 'AWS_SECRET_ACCESS_KEY'
PRI_BUCKET_NAME = 's3-sourcedata-petproject'

def create_bucket(name, s3, secure = False):
    try:
        s3.create_bucket(Bucket=name,
                        CreateBucketConfiguration={
                            'LocationConstraint': 'us-east-1'}
                        )
        if secure:
            prevent_public_access(name, s3)
    except ClientError as ce:
        print('error', ce)

def prevent_public_access(bucket, s3):
    try:
        s3.meta.client.put_public_access_block(Bucket = bucket,
            PublicAccessBlockConfiguration = {
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            })
    except ClientError as ce:
        print('error: ', ce)

def delete_bucket(bucket, s3):
    try:
        s3.Bucket(bucket).delete()
    except ClientError as ce:
        print('error: ', ce)

def main():
    access = os.getenv(ACCESS_KEY)
    secret = os.getenv(SECRET_KEY)
    s3 = boto3.resource('s3', aws_access_key_id=access, aws_secret_access_key=secret)

    create_bucket(PRI_BUCKET_NAME, s3, True)

    #delete_bucket(PRI_BUCKET_NAME, s3)

if __name__ == '__main__':
    main()
