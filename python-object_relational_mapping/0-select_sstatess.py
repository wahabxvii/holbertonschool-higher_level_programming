#!/usr/bin/python3
from sqlalchemy import create_engine
import MySQLdb


engine = create_engine("mysql://root:pass@localhost/mydb")
engine.connect()
