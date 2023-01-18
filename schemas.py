# -*- coding:utf-8 -*-

from typing import Any, Union, List, Optional
from pydantic import BaseModel, Field, ValidationError, validator


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None



class UserBase(BaseModel):
    user_name: str
    email: Optional[str]

    @validator('user_name')
    def user_name_must_be_alphanumeric_and_len_between_four_and_sixteen(cls, v):
        # 用户名只能是字母或数字
        if not v.isalnum():
            raise ValueError('must be alphanumeric')
        # 长度检查
        if len(v) < 4 or len(v) > 16:
            raise ValueError('must be between 4 and 16 characters')
        return v

    @validator('email')
    def email_must_be_valid(cls, v):
        if not is_email(v):
            raise ValueError('must be a valid email address')
        return v


class UserRegister(UserBase):
    password: str = Field(..., min_length=6, max_length=16)
    tags: List[str] = Field(..., min_items=1, max_items=11)
    field_code: int

    @validator('password')
    def password_must_be_len_between_six_and_sixteen(cls, v):
        if len(v) < 6 or len(v) > 16:
            raise ValueError('must be between 6 and 16 characters')
        return v
