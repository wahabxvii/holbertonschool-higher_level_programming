#!/usr/bin/python3
'''python file contain class definition of state'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# DATABASE_URL = 'mysql+pymysql://3306/mydatabase'
# engine = create_engine(DATABASE_URL)
# Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class state(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

# Base.metadata.create_all(engine)
