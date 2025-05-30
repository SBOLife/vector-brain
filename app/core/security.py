"""Security module for JWT token handling and authentication.

This module provides functionality for creating and managing JWT access tokens
for user authentication and authorization. It includes utilities for token
generation with configurable expiration times.
"""

from datetime import datetime, timedelta
import jwt
from app.core.config import JWT_ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, JWT_SECRET_KEY


def create_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
):
    """
    Create a new JWT access token.

    This function generates a JSON Web Token (JWT) that can be used for authenticated
    API requests. The token includes the provided data along with an expiration time.

    Parameters:
    -----------
    data : dict
        The payload data to encode in the token. This typically includes user
        identification information such as user_id or username.

    expires_delta : timedelta, optional
        The time until the token expires. Defaults to ACCESS_TOKEN_EXPIRE_MINUTES
        from configuration.

    Returns:
    --------
    str
        The encoded JWT token string.

    Example:
    --------
    >>> user_data = {"sub": "user@example.com", "user_id": 123}
    >>> token = create_access_token(user_data)
    >>> token = create_access_token(user_data, timedelta(hours=1))
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
