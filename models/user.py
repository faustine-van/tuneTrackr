#!/usr/bin/env python3
""" User model """
import bcrypt
from flask import current_app as app
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from itsdangerous import URLSafeTimedSerializer as Serializer
from models.base import Base, BaseTune


class User(BaseTune, Base):
    """User Class"""

    __tablename__ = "users"
    firstname = Column(String(128), nullable=True)
    lastname = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    password = Column(String(255), nullable=False)

    # Relationship
    roles = relationship("Role", secondary="user_roles")

    def __init__(self, *args, **kwargs) -> None:
        """Initialize a User instance"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, val):
        """Setter of password and encrypt it using bcrypt

        Args:
            passwd (str): Password to be encrypted
        """
        if name == "password" and val is not None:
            byte_pass = val.encode("utf-8")
            gen_salt = bcrypt.gensalt()
            val = bcrypt.hashpw(byte_pass, gen_salt)
        super().__setattr__(name, val)

    def is_validpassword(self, pwd: str) -> bool:
        """check the provided password if
            matches the hashed password.

        Args:
            pwd (string): password to for check
                If not provided, return None.
            hashed_pwd (string): hashed passwprd
        Returns:
                if match return True if not match return False
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        try:
            # convert password to bytes
            bytes_pass = pwd.encode("utf-8")
            bytes_hashed_password = self.password.encode("utf-8")
            is_valid = bcrypt.checkpw(bytes_pass, bytes_hashed_password)
            return is_valid
        except ValueError:
            return False

    def get_reset_token(self):
        """get reset token
        Args:
            exp_sec (timestamp): expiration time
        """
        s_obj = Serializer(app.config["JWT_SECRET_KEY"])
        return s_obj.dumps({"user_id": self.id})

    @staticmethod
    def verify_reset_token(token, exp_sec=1800):
        """verify reset token
        Args:
            token (timestamp): provided token
        """
        s_obj = Serializer(app.config.get("JWT_SECRET_KEY"))
        try:
            user_id = s_obj.load(token, exp_sec)["user_id"]
        except Exception:
            return None
        return User.query.get(user_id)

    def has_role(self, role):
        """check if user has role
        Args:
            role (str): providedrole
        """
        return any(user_role.name == role for user_role in self.roles)


class Role(BaseTune, Base):
    """Role Class"""

    __tablename__ = "roles"
    name = Column(String(50), unique=True)


class UserRole(BaseTune, Base):
    """Role Class"""

    __tablename__ = "user_roles"
    user_id = Column(String(60), ForeignKey("users.id", ondelete="CASCADE"))
    role_id = Column(String(60), ForeignKey("roles.id", ondelete="CASCADE"))
