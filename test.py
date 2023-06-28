import boto3
import streamlit as st

AWS_REGION ="ap-northeast-1"
bucket_name = st.secrets.AWS_KEYS.bucket_name
url_api = "https://e48ajtso28.execute-api.ap-northeast-1.amazonaws.com/dev"
service_name = 's3'
access_key = st.secrets.AWS_KEYS.AWS_ACCESS_KEY_ID
secret_key = st.secrets.AWS_KEYS.AWS_SECRET_ACCESS_KEY


s3_resource = boto3.resource(service_name, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
bucket = s3_resource.Bucket(bucket_name)

print("object delete ...")
for obj in bucket.objects.all():
    responce = bucket.delete_objects(
        Delete={
            "Objects": [
                {"Key":obj.key}
            ]
        }
    )
print(responce)