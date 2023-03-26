import boto3
import streamlit as st

AWS_REGION ="ap-northeast-1"
bucket_name = st.secrets.AWS_KEYS.bucket_name
url_api = "https://e48ajtso28.execute-api.ap-northeast-1.amazonaws.com/dev"
service_name = 's3'
access_key = st.secrets.AWS_KEYS.AWS_ACCESS_KEY_ID
secret_key = st.secrets.AWS_KEYS.AWS_SECRET_ACCESS_KEY


s3_resource = boto3.resource(service_name, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

s3_object = s3_resource.Object(bucket_name,'file.midi')

s3_object.delete()

print("s3バケットからファイルの削除が完了しました")