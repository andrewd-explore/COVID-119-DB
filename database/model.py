from botocore.errorfactory import ClientError
from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, String, Date, ForeignKey, DateTime, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import boto3
import base64
from botocore.exceptions import ClientError
import json

Base = declarative_base()


class CasesGlobal(Base):
    __tablename__ = 'CasesGlobal'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    confirmed = Column(Integer)
    deaths = Column(Integer)
    recovered = Column(Integer)

    country_id = Column(Integer, ForeignKey('Country.id'))
    
    
class CounterMeasures(Base):
    __tablename__ = 'CounterMeasures'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    measure = Column(String)
    value = Column(Float)
    country_id = Column(Integer, ForeignKey('Country.id'))


class Country(Base):
    __tablename__ = 'Country'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    lat = Column(Float)
    long = Column(Float)


class Location(Base):
    __tablename__ = 'Location'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('Country.id'))
    location = Column(String)
    location_level = Column(String)


class CasesLocal(Base):
    __tablename__ = 'CasesLocal'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    confirmed = Column(Integer)
    location_id = Column(Integer, ForeignKey('Location.id'))


class Tests(Base):
    __tablename__ = 'Tests'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    cumulative_tests = Column(Integer)
    country_id = Column(Integer, ForeignKey('Country.id'))


    
    
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


if __name__ == "__main__":
    secret = json.loads(get_secret()["SecretString"]

    engine = create_engine(
        'mssql+pymssql://' +
        secret['username'] + ':' + secret['password'] + '@' + secret['host'] + ':' +
        str(secret['port']) + '/Corona'

    )

    Base.metadata.create_all(engine)
