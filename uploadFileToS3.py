import os
import boto3
from botocore.exceptions import ClientError

ACCESS_KEY = 'AWS_ACCESS_KEY_ID'
SECRET_KEY = 'AWS_SECRET_ACCESS_KEY'
BUCKET_NAME = 's3-sourcedata-petproject'
file = '2019_Oscars.csv'
DIR = "."

def upload_file(bucket, directory, file, s3, s3path=None):
    file_path = directory + '//' + file
    remote_path = s3path
    if remote_path is None:
        remote_path = file
    try:
        s3.Bucket(bucket).upload_file(file_path, remote_path)
    except ClientError as ce:
        print('error', ce)

def main():
    access = os.getenv(ACCESS_KEY)
    secret = os.getenv(SECRET_KEY)
    s3 = boto3.resource('s3', aws_access_key_id=access, aws_secret_access_key=secret)

    upload_file(BUCKET_NAME, DIR, file, s3)

if __name__ == '__main__':
    main()
