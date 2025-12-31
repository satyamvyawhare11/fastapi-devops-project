import boto3

def read_s3_buckets():
    client = boto3.client("s3")
    response = client.list_buckets()

    bucket_list = []

    for bucket in response["Buckets"]:
        bucket_list.append(bucket["Name"])

    return {
        "count": len(bucket_list),
        "names": bucket_list
    }
