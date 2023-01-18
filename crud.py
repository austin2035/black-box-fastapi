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


def get_box_number(db: Session, gender: int):
    """[Atomic] 获取某性别的盲盒数量"""
    return db.query(func.count('*')).select_from(models.Box).filter(models.Box.gender == gender).scalar()


def add_box(db: Session, box: schemas.BoxCreate):
    """[Atomic] 添加盲盒"""
    data = box.dict()
    data['gender'] = True if data['gender'] == 1 else False
    try:
        db_box = models.Box(**data)
        db.add(db_box)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return db_box


def update_box(db: Session, box_id: int, visitor_id: str):
    """[Atomic] 更新盲盒"""
    db.query(models.Box).filter(models.Box.id == box_id).update({'is_selected': True, 'select_visitor_id': visitor_id})
    db.commit()
    return True


def get_visitor_raffle_number(db: Session, visitor_id: str):
    """[Atomic] 获取访客的抽奖次数"""
    return db.query(func.count('*')).select_from(models.Box).filter(models.Box.select_visitor_id == visitor_id).scalar()


def get_a_box(db: Session, gender: int):
    """[Atomic] 抽取一个相反性别的盲盒"""
    return db.query(models.Box).filter(models.Box.is_selected == False, models.Box.gender == gender).first()


