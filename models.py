# -*- coding:utf-8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(64), unique=True, index=True)
    create_time = Column(Integer)
    update_time = Column(Integer)
