# -*- coding:utf-8 -*-

from sqlalchemy import Boolean, Column, Integer, String, CHAR
from database import Base


class Box(Base):
    __tablename__ = "box"

    id = Column(Integer, primary_key=True, index=True)
    wechat = Column(String(64), unique=True, index=True)
    gender = Column(CHAR(1))
    age = Column(Integer)
    desc = Column(String(256))
    status = Column(Boolean, default=False, index=True)
    depositor_id = Column(CHAR(32))
    extractor_id = Column(CHAR(32), index=True)
    # rank， 可抽取次数
    rank = Column(Integer, default=0, index=True)
    # 用户投放时间
    put_time = Column(Integer, index=True)



