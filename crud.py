# -*- coding:utf-8 -*-
import math

from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from database import engine
from pymysql.converters import escape_string
import schemas
import models


def get_user_by_user_name(db: Session, user_name: str):
    """[Atomic] 通过用户名获取用户信息 """
    return db.query(models.User).filter(models.User.user_name == user_name).first()
