import boto3

# insecure code for demo purposes. Keys are not real.
s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYY',
    region_name='us-east-1'
)

# Initialize the S3 client
s3 = boto3.client('s3')

# Define your S3 bucket name, object key (file name in S3), and local file path
bucket_name = 'ghas-demo-s3'
s3_object_key = 'path/to/your/file.txt'  # e.g., 'documents/report.pdf'
local_file_path = 'local_copy_of_file.txt'

try:
    s3.download_file(bucket_name, s3_object_key, local_file_path)
    print(f"File '{s3_object_key}' downloaded successfully to '{local_file_path}'")
except Exception as e:
    print(f"Error downloading file: {e}")
