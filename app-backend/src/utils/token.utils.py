import jwt
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Annotated
# insert secret_key later from .env
class Token(BaseModel):
    access_token: str
    token_type: str


class Token_Data(BaseModel):
    email: str
    user_id: str


def create_access_token(data: dict, expires_delta:timedelta):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp":expires_delta})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




