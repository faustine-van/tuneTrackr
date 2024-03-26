#!/usr/bin/python3
"""1-main module"""
from models.user import User
from models import dbStorage
from models.auth import TokenBlockList
from datetime import datetime

# Create instances of User and TokenBlockList
user = User(
    firstname="John", lastname="Doe", email="john@example.com",
    password="12334"
)
user.save()
users = dbStorage.search(User, {"email": "john@example.com"}).values()

for user in users:
    token_blocklist = TokenBlockList(
        jti="unique_jti",
        token_type="access_token",
        user_id=user.id,
        revoked_at=None,
        expires=datetime.utcnow(),
    )
    token_blocklist.save()
