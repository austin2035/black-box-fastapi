# -*- coding:utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
import schemas
from database import engine
from routers import user
import crud
from deps import get_db
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "https://togetherblackbox.com",
    "https://dev.togetherblackbox.com",
    "https://www.togetherblackbox.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router, prefix="/user", tags=["user"])


@app.get("/")
async def get_root():
    return schemas.Response()


@app.put("/box")
async def put_box(box: schemas.BoxCreate, db: Session = Depends(get_db)):
    """添加盲盒"""
    try:
        crud.add_box(db, box)
    except Exception as e:
        print(e)
    return schemas.Response()


@app.get("/box/count/{visitor_id}")
def get_available_box_number(visitor_id: str, db: Session = Depends(get_db)):
    count = crud.get_available_box_number(db, visitor_id)
    return schemas.Response(data=count)


@app.get("/box/{visitor_id}")
def extract_box_for_visitor(visitor_id: str, db: Session = Depends(get_db)):
    # 为访客抽取一个盲盒
    data = crud.get_available_box_for_visitor(db, visitor_id)
    print(data)

    # 如果没有可用盲盒
    if not data:
        visitor = crud.get_visitor_data(db, visitor_id)
        # 如果访客是男性，那么就返回固定值
        if visitor and visitor.gender == '1':
            return schemas.Response(data={'age': 25, 'gender': '2', 'wechat': 'dece38'})

        # 如果访客是女性，就没有可用的盲盒
        return schemas.Response(code=1, msg="没有可用的盲盒")

    return schemas.Response(data=data)

