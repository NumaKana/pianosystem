import boto3

AWS_REGION ="ap-northeast-1"
bucket_name = "lilycompile-save-tmp"

s3_resource = boto3.resource('s3',region_name=AWS_REGION)

s3_object = s3_resource.Object(bucket_name,'test5.pdf')

s3_object.download_file(r'./test_download.pdf')

print("s3バケットからのファイルアップロードが完了しました")