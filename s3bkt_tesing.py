import boto3

# AWS S3 credentials and configuration
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = 'onlineshops3bkt'
AWS_S3_REGION_NAME = 'ap-south-1'

# Initialize S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_REGION_NAME
)

# Test the connection
try:
    response = s3_client.list_buckets()
    print("Successfully connected to S3!")
    for bucket in response['Buckets']:
        print(f' - {bucket["Name"]}')
except Exception as e:
    print(f"Failed to connect to S3: {e}")
