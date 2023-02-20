# -*- coding:utf-8 -*-

import time
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from deps import get_db
import crud
import schemas

router = APIRouter()


@router.get("/visitor/{visitor_id}")
async def fetch_visitor_data(visitor_id: str, db: Session = Depends(get_db)):
    """获取访客的信息，通过访客id"""
    data = crud.get_visitor_data(db, visitor_id)
    if not data:
        return schemas.Response(code=1, msg="访客不存在", data=None)
    return schemas.Response(data=data)


@router.patch("/visitor/reset")
async def update_visitor_data(visitor_id: schemas.VisitorID, db: Session = Depends(get_db)):
    visitor_id = visitor_id.dict().get("visitor_id")
    """更新访客的信息，通过访客id"""
    data = crud.get_visitor_data(db, visitor_id)
    if not data:
        return schemas.Response(code=1, msg="访客不存在", data=False)
    crud.reset_visitor(db, visitor_id)
    result = crud.get_visitor_data(db, visitor_id)
    return schemas.Response(data=result)


