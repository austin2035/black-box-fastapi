# -*- coding:utf-8 -*-
import math

from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from database import engine
from pymysql.converters import escape_string
import schemas
import models


def add_box(db: Session, box: schemas.BoxCreate):
    """[Atomic] 添加盲盒"""
    data = box.dict()
    data['status'] = False
    try:
        print(data)
        db_box = models.Box(**data)
        db.add(db_box)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return db_box


def update_box(db: Session, box_id: int, visitor_id: str):
    """[Atomic] 更新盲盒"""
    db.query(models.Box).filter(models.Box.id == box_id).update({'status': True, 'extractor_id': visitor_id})
    db.commit()
    return True


def get_visitor_extract_number(db: Session, visitor_id: str):
    """获取访客抽取次数"""
    return db.query(models.Box).filter(models.Box.extractor_id == visitor_id).count()


def get_visitor_data(db: Session, visitor_id: str):
    """获取访客的信息，通过访客id"""
    return db.query(models.Box).filter(models.Box.depositor_id == visitor_id).first()


def get_available_box_number(db: Session, visitor_id: str):
    """获取可用盲盒数量"""
    data = get_visitor_data(db, visitor_id)
    if not data:
        return 0
    target_gender = '2' if data.gender == '1' else '1'
    return db.query(models.Box).filter(models.Box.gender == target_gender, models.Box.status == False).count()


def get_available_box_for_visitor(db: Session, visitor_id: str):
    # 抽取一个盲盒
    data = get_visitor_data(db, visitor_id)

    # 检查是否存在此用户
    if not data:
        return None
    count = get_available_box_number(db, visitor_id)

    # 检查可用数量
    if count == 0:
        return None

    target_gender = '2' if data.gender == '1' else '1'

    res = db.query(models.Box).filter(
        models.Box.gender == target_gender,
        models.Box.status == False,
        models.Box.age.between(data.age - 5, data.age + 5)
    ).limit(1).first()
    if not res:
        return None
    result = {'age': res.age, 'gender': res.gender, 'wechat': res.wechat}
    # 更新盲盒信息
    update_box(db, res.id, visitor_id)
    return result
