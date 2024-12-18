from dotenv import load_dotenv
import boto3
import os
load_dotenv()


def connect_s3():
    client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name='ap-northeast-1'
    )
    print("S3 Client created successfully.")
    print(client.list_buckets())
    return client


def upload_file_to_s3(filename, bucket, key):
    client = connect_s3()
    if client:
        print("S3 Client created successfully.")
        print(client.list_buckets())
        client.upload_file(filename, bucket, key)
        print(f"File {filename} uploaded successfully to {bucket}/{key}.")
    else:
        print("Failed to create S3 client.")

Filename = 'your-file-name'
Bucket = 'your-bucket-name'
Key = 'your-file-name' #key is the name of the file in the bucket


upload_file_to_s3(Filename, Bucket, Key)
