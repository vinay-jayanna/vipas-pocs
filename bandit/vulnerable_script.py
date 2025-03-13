import subprocess
import requests
import boto3

def list_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        print(f"Bucket Name: {bucket['Name']}")

def insecure_subprocess(user_input):
    # Vulnerable to command injection
    subprocess.call(f"echo {user_input}", shell=True)

def insecure_http_request():
    response = requests.get("http://example.com")
    print(response.text)

if __name__ == "__main__":
    list_buckets()
    user_input = input("Please enter a command: ")
    insecure_subprocess(user_input)
    insecure_http_request()

