#!/usr/bin/env python3
"""generate jwt_token"""

import secrets

jwt_secret_key = secrets.token_urlsafe(32)
print(jwt_secret_key)
