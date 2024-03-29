import boto3
import requests
import subprocess
import streamlit as st
import os
import glob
 

AWS_REGION ="ap-northeast-1"
bucket_name = st.secrets.AWS_KEYS.bucket_name
url_api = "https://e48ajtso28.execute-api.ap-northeast-1.amazonaws.com/dev/"
service_name = 's3'
access_key = st.secrets.AWS_KEYS.AWS_ACCESS_KEY_ID
secret_key = st.secrets.AWS_KEYS.AWS_SECRET_ACCESS_KEY

def mxl_ly(file):
    subprocess.run("python musicxml2ly/musicxml2ly.py --output=file/file " + file, shell=True)

def make_png(dir):
    remove(dir)
#    subprocess.run("lilypond --formats=png -o "+ dir +"/file "+dir+"/file.ly", shell=True)

# -----------手元で動かすときはここをコメントアウト---------------
    data = open(dir+"/file.ly", 'r', encoding="utf-8")
    payload = {
        'code': data.read(),
        'id':'file'
    }
    print("api request...")
    r = requests.post(url_api, json=payload)
    get_from_s3(dir)
# ---------------------------------------------------------

def remove(dir):
    for filename in  glob.glob(dir+'/*.png'):
        os.remove(filename)   

def get_from_s3(dir):
    s3_resource = boto3.resource(service_name, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    bucket = s3_resource.Bucket(bucket_name)
    print("object download ...")
    for obj in bucket.objects.all():
        s3_object = s3_resource.Object(bucket_name,obj.key)
        s3_object.download_file(dir+"/"+obj.key)
    print("done!")



#print("s3バケットからのファイルアップロードが完了しました")