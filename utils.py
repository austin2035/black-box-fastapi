# -*- coding=utf-8

import base64
import os
import re
import sys
from datetime import datetime, timedelta
from typing import Union, Any

import pytz
from jose import jwt
from passlib.context import CryptContext

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 14  # 14 days
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 14  # 14 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv("jwt_key")
JWT_REFRESH_SECRET_KEY = os.getenv("jwt_refresh_key")


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def is_email(email: str) -> bool:
    """
    判断是否为邮箱
    :param email:
    :return:
    """
    if re.match(r"^(([^<>()\[\]\\.,;:\s@']+(\.[^<>()\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,"
                r"3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$", email) is not None:
        return True
    return False


def is_username(username: str) -> bool:
    """
    判断是否为用户名
    :param username:
    :return:
    """
    if re.match("^[a-zA-Z0-9_-]{4,16}$", username) is not None:
        return True
    return False

def is_today(timestamp) -> bool:
    """
    判断是否为今天, pytz 指定加拿大多伦多时区
    :param timestamp:
    :return:
    """
    today = datetime.now(pytz.timezone("Canada/Eastern")).date()
    if timestamp.date() == today:
        return True
    return False
