from botocore.errorfactory import ClientError
from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, String, Date, ForeignKey, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import json

if __name__ == "__main__":

    secret = {
        "username": "admin",
        "password": "corona_must_die",
        "host": "database-1.ccwgqdqrrmvt.eu-west-1.rds.amazonaws.com",
        "port": "1433"
    }

    engine = create_engine(
        'mssql+pymssql://' +
        secret['username'] + ':' + secret['password'] + '@' + secret['host'] + ':' +
        str(secret['port']),
        connect_args={'autocommit': True}
    )

    engine = create_engine(
        'mssql+pymssql://' +
        secret['username'] + ':' + secret['password'] + '@' + secret['host'] + ':' +
        str(secret['port']) + '/Corona'

    )



    Base = declarative_base()


    class Cases(Base):
        __tablename__ = 'Cases'

        id = Column(Integer, primary_key=True)
        date = Column(Date)
        confirmed = Column(Integer)
        deaths = Column(Integer)
        recovered = Column(Integer)

        country_id = Column(Integer, ForeignKey('Country.id'))


    class Country(Base):
        __tablename__ = 'Country'

        id = Column(Integer, primary_key=True)
        country = Column(String)

    class Location(Base):
        __tablename__ = 'Location'

        id = Column(Integer, primary_key=True)
        country_id = Column(Integer, ForeignKey('Country.id'))
        location = Column(String)
        location_level = Column(String)

    class Patients(Base):
        __tablename__ = 'ConfirmedPatients'

        id = Column(Integer, primary_key=True)
        date = Column(Date)
        age = Column(Integer)
        gender = Column(Integer)
        travel_status = Column(String)
        location_id = Column(Integer, ForeignKey('Location.id'))







    #
    # class Comment(Base):
    #     __tablename__ = 'Comments'
    #
    #     id = Column(Integer, primary_key=True)
    #     date = Column(Date)
    #     commenter = Column(String)
    #     comment = Column(String)
    #
    #     feature_id = Column(Integer, ForeignKey('Feature.id'))
    #     feature = relationship("Feature")
    #
    #
    # class JobLog(Base):
    #     __tablename__ = 'JobLog'
    #
    #     id = Column(Integer, primary_key=True)
    #
    #     concept_id = Column(Integer, ForeignKey('Concept.id'))
    #     concept = relationship("Concept")
    #
    #     user_identifier = Column(String)
    #
    #     has_started = Column(Boolean)
    #     has_completed = Column(Boolean)
    #
    #     timestamp_started = Column(DateTime)
    #     timestamp_completed = Column(DateTime)
    #
    Base.metadata.create_all(engine)
