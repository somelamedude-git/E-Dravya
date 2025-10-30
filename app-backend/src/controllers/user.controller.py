from ../utils/password.utils import verify_password, get_password_hash
import jwt
from fastapi import Depends, FastAPI, HTTPException, status, Response, Cookie
from fastapi.security import OAuth2PasswordBearer, OAuth2Password
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from ../models/user.model import User
from ../utils/token.utils import create_access_token

def authenticate_user(email, password, session):
    user_ = session.query(User).filter_by(email=email).first()
    if not user_:
        raise HTTPException(
                status_code=404,
                detail="Recheck your credentials"
                )

    correct_password = verify_password(password, user_.password)
    if not correct_password:
        raise HTTPException(
                status_code=401,
                detail ="Recheck your credentials"
                )

    return user_

def authenticate_with_token(form_data, session, response: Response):
    user_ = authenticate_user(form_data.email, form_data.password,  session)
    username = user_.username

    data = {
            "username":username,
            "email": form_data.email
            }
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data, access_token_expires)

    response.set_cookie(
            key="access_token",
            value=access_token,
            httpOnly=True,
            max_age=access_token_expires*60,
            samesite="lax",
            secure=False
            )




