"""This module defines the authentication endpoints for the API."""

from datetime import timedelta

import bcrypt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from simple_webapp_k8s.auth_utils import Token, create_access_token
from simple_webapp_k8s.conf import settings

router = APIRouter(tags=["authentication"])

TEST_PASSWORD = "password123"
SALT = bcrypt.gensalt()
HASHED_PASSWORD = bcrypt.hashpw(TEST_PASSWORD.encode("utf-8"), SALT)

FAKE_USERS_DB = {
    "testuser": {"username": "testuser", "hashed_password": HASHED_PASSWORD}
}

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token", description="JWT token authentication"
)


def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    """
    Verifies that a plain text password matches its hashed version.

    Args:
        plain_password (str): The plain text password to verify.
        hashed_password (bytes): The hashed password to compare against.

    Returns:
        bool: True if the plain password matches the hashed password, otherwise False.
    """
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)


@router.post(
    "/token",
    response_model=Token,
    summary="Create access token",
    description="""
    Login with username and password to get JWT token.
    
    Test credentials:
    - Username: testuser
    - Password: password123
    """,
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    Login with username and password to get JWT token.

    Test credentials:
    - Username: testuser
    - Password: password123

    Args:
        form_data (OAuth2PasswordRequestForm): The form data containing the username and password.

    Returns:
        Token: A JWT token with the user's username as the subject.

    Raises:
        HTTPException: If the username or password is incorrect.
    """

    user = FAKE_USERS_DB.get(form_data.username)
    if not user or not verify_password(
        form_data.password, user["hashed_password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
