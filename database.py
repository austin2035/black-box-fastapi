# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

MYSQL_PASSWORD = os.getenv("mysql_password")
MYSQL_USERNAME = os.getenv("mysql_username")
MYSQL_HOST = os.getenv("mysql_host")
MYSQL_DATABASE_NAME = os.getenv("mysql_database_name")
print("MySQL INFO:", MYSQL_PASSWORD, MYSQL_USERNAME, MYSQL_HOST, MYSQL_DATABASE_NAME)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
