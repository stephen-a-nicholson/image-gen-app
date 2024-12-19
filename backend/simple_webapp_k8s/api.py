"""This module defines the FastAPI application and includes the routers"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from simple_webapp_k8s.routers import auth, hello

app = FastAPI(title="Hello World API")


@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """
    This middleware adds security headers to the response.

    The following headers are added:

    - X-Content-Type-Options: nosniff
    - X-Frame-Options: DENY
    - X-XSS-Protection: 1; mode=block
    - Strict-Transport-Security: max-age=31536000; includeSubDomains

    These headers are added to help prevent common web attacks such as
    cross-site scripting (XSS) and clickjacking.

    The Strict-Transport-Security header is added to ensure that the API
    is only accessed over HTTPS.
    """
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains"
    )
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(hello.router)
