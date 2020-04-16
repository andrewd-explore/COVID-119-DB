from chalice import Chalice
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import boto3
import base64
from botocore.exceptions import ClientError
import json

app = Chalice(app_name='covid19')


def get_secret():
    secret_name = "SecretCorona"
    region_name = "eu-west-1"
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    return get_secret_value_response

secret = json.loads(get_secret()["SecretString"])


username = secret['username']
password = secret['password']
host = secret['host']
port = secret['port']

engine = create_engine(
    'mssql+pymssql://' +
    username + ':' + password + '@' + host + ':' +
    str(port) + '/Corona'

)

@app.route('/',api_key_required=True)
def index():
    return 'Covid 19 rest API'


@app.route('/get_table/{table_name}',api_key_required=True)
def get_table(table_name):

    table_name = table_name.replace('%22','')

    sql_query = "Select * from " + table_name
    results_proxy = engine.execute(sql_query)

    d,a = {},[]
    for rowproxy in results_proxy:
        for column,value in rowproxy.items():
            d = {**d,**{column:value}}
        a.append(d)

    return a



