from ../utils/password.utils import verify_password, get_password_hash
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2Password
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from ../models/user.model import User

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





