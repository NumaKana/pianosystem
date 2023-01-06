import boto3
import requests
import subprocess

AWS_REGION ="ap-northeast-1"
bucket_name = "lilycompile-save-tmp"
url_api = "https://e48ajtso28.execute-api.ap-northeast-1.amazonaws.com/dev"
url_s3 = "s3://arn:aws:s3:ap-northeast-1:880991079725:accesspoint/accesspoint"
service_name = 's3'
access_key = 'AKIA42HZJBUWZWKL4KE4'
secret_key = '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'

def mxl_ly():
    subprocess.run("python musicxml2ly/musicxml2ly.py --output=file/file sheet/file.mxl", shell=True)

def make_png(dir):
    data = open(dir+"/file.ly", 'r', encoding="utf-8")
    payload = {
        'code': data.read(),
        'id':'file'
    }
    print("api request...")
    r = requests.post(url_api, json=payload)
    print("done!")
    get_from_s3(dir)


def get_from_s3(dir):
    s3_resource = boto3.resource(service_name, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    bucket = s3_resource.Bucket(bucket_name)
    print("object download ...")
    for obj in bucket.objects.all():
        s3_object = s3_resource.Object(bucket_name,obj.key)
        s3_object.download_file(dir+"/"+obj.key)
    print("done!")


#print("s3バケットからのファイルアップロードが完了しました")