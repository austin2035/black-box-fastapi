# -*- coding:utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
import schemas
from database import engine
from routers import user, upload, setting, links, theme

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

