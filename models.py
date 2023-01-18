# -*- coding:utf-8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR
from database import Base


class Box(Base):
    __tablename__ = "box"

    id = Column(Integer, primary_key=True, index=True)
    wx_id = Column(String(64), unique=True, index=True)
    gender = Column(Boolean)
    age = Column(Integer)
    desc = Column(String(256))
    is_selected = Column(Boolean, default=False, index=True)
    visitor_id = Column(String(32))
    select_visitor_id = Column(String(32), index=True)
