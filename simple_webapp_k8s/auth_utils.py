"""This module contains utility functions for authentication and token handling."""

from datetime import datetime, timedelta
from typing import Optional

import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel

from simple_webapp_k8s.conf import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    """A Pydantic model representing a JWT token."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """A Pydantic model representing token data."""

    username: Optional[str] = None


def get_password_hash(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the hashed password.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def create_access_token(
    data: dict, expires_delta: Optional[timedelta] = None
) -> str:
    """
    Creates a JSON Web Token (JWT) for a given set of data with an optional expiration time.

    Args:
        data (dict): The data to include in the payload of the token.
        expires_delta (Optional[timedelta]): An optional timedelta
        indicating the token's expiration time.
            If not provided, the token will expire in 15 minutes by default.

    Returns:
        str: The encoded JWT as a string.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Retrieves the username from a given JWT token.

    This function takes an optional JWT token as a parameter and returns the username
    stored in the token's payload. If the token is invalid or missing, it raises an
    HTTPException with a 401 status code.

    Args:
        token (str, optional): The JWT token to parse. Defaults to None.

    Returns:
        str: The username stored in the token's payload.

    Raises:
        HTTPException: If the token is invalid or missing.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError as exc:
        raise credentials_exception from exc
    return token_data.username
