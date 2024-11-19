""" This module defines the root and health check endpoints for the API."""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from simple_webapp_k8s.auth_utils import get_current_user

router = APIRouter()


@router.get("/", response_class=JSONResponse)
async def root(current_user: str = Depends(get_current_user)):
    """
    Root endpoint that returns a greeting message for the current user.

    This endpoint requires authentication and retrieves the current user
    from the access token. It returns a JSON response with a personalized
    greeting message.

    Args:
        current_user (str): The username of the authenticated user.

    Returns:
        JSONResponse: A JSON response containing a greeting message.
    """
    return {"message": f"Hello, {current_user}!"}


@router.get("/health")
async def health_check():
    """
    Returns a simple JSON response with a 'healthy' status.

    This endpoint is the health check point for the API and is intended to be
    used by external systems to verify that the API is operational.
    """
    return {"status": "healthy"}
