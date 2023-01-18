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
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_root():
    return schemas.Response()


@app.post("/raffle_box")
async def raffle_box(box: schemas.BoxCreate, db: Session = Depends(get_db)):
    # 添加盲盒
    try:
        crud.add_box(db, box)
    except Exception as e:
        print("添加盲盒失败", e)


    turn_gender = 0 if box.gender else 1

    # 获取盲盒数量
    box_number = crud.get_box_number(db, turn_gender)
    if box_number == 0:
        return schemas.Response(code=1, msg="相反性别盲盒数量为0")

    # 获取访客的抽奖次数
    visitor_raffle_number = crud.get_visitor_raffle_number(db, box.visitor_id)
    if visitor_raffle_number >= 1:
        return schemas.Response(code=2, msg="该访客已经抽取过")

    # 抽取盲盒
    box_new = crud.get_a_box(db, turn_gender)
    data = {"gender": "男" if box_new.gender else "女", "wx_id": box_new.wx_id, "age": box_new.age, "desc": box_new.desc}
    # 更新盲盒
    crud.update_box(db, box_new.id, box.visitor_id)

    return schemas.Response(data=data)