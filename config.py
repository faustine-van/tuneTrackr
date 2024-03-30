#!/usr/bin/env python3
""" config.py """
import os

from dotenv import load_dotenv


# load env variables from .env file
load_dotenv()


class Config:
    """configuration variables"""

    # DATABASE
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_TUNETRACKR = os.getenv("DB_TUNETRACKR")
    DB_HOST = os.getenv("DB_HOST")
    # API
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = os.getenv("API_PORT", 5000)
    DEBUG = os.getenv("DEBUG", False)
    # SECURITY
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    # main
    MAIL_DEBUG = os.getenv("MAIL_DEBUG")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    # MAIL_USE_SSL=False
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
