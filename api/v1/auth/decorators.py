#!/usr/bin/python3
""" decorators """
from functools import wraps
from flask_jwt_extended import get_current_user


def auth_role_required(*roles):
    """decorators for roles"""

    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            current_user = get_current_user()
            if current_user is None:
                return {"msg": "User not found"}, 404
            if any(current_user.has_role(r) for r in roles):
                return fn(*args, **kwargs)
            else:
                return {"msg": f"Missing roles {','.join(roles)}"}, 403

        return decorator

    return wrapper


def auth_role(role):
    """decorators for roles"""

    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            current_user = get_current_user()
            roles = role if isinstance(role, list) else [role]
            if all(not current_user.has_role(r) for r in roles):
                return {"msg": f"Missing roles {','.join(roles)}"}, 403
            return fn(*args, **kwargs)

        return decorator

    return wrapper


def admin_required(fn):
    """decorators for admin only"""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_current_user()
        if current_user.has_role("admin"):
            return fn(*args, **kwargs)
        else:
            return {"msg": "Insufficient permissions for role 'admin'"}, 403

    return wrapper
