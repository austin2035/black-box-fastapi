# -*- coding:utf-8 -*-

from sqlalchemy import Boolean, Column, Integer, String, CHAR
from database import Base


class Box(Base):
    __tablename__ = "box"
    id = Column(Integer, primary_key=True, index=True)
    depositor_id = Column(CHAR(32))
    # 剩余抽取次数
    rank = Column(Integer, default=0, index=True)
    # 上次投放时间
    last_put_time = Column(Integer, index=True)
    wechat = Column(String(64), unique=True, index=True)
    gender = Column(CHAR(1))
    age = Column(Integer)
    # 此盲盒抽取状态
    status = Column(Boolean, default=False, index=True)
    extractor_id = Column(CHAR(32), index=True)
