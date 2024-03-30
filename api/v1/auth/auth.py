#!/usr/bin/python3
""" objects that handle all authentication of RestFul API"""
import datetime

# from threading import Thread
from flask_mail import Message, Mail
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    decode_token,
    jwt_required,
    get_current_user,
    get_jwt_identity,
    get_jwt,
)
from flask import current_app as app
from flask import jsonify, request, url_for
from flasgger import swag_from
from werkzeug.exceptions import InternalServerError
from models.user import User
from models import dbStorage
from api.v1.auth import auth_s
from exts import jwt
from api.v1.auth.decorators import auth_role
from api.v1.auth.helpers import (
    add_token_to_db,
    revoke_token,
    is_token_revoked,
)
from api.v1.auth.docs.auth_user import (
    register_swagger,
    login_swagger,
    logout_swagger,
    profile_swagger,
    refresh_swagger,
    revoke_access_swagger,
    revoke_refresh_swagger,
    forget_password_swagger,
    reset_password_swagger,
)


@auth_s.route("/register", methods=["POST"], strict_slashes=False)
@swag_from(register_swagger)
def post_user():
    """
    Create a user
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    if not data.get("email"):
        return jsonify({"msg": "Missing email"}), 400
    if not data.get("password"):
        return jsonify({"msg": "Missing password"}), 400

    # Check if email already exists
    if dbStorage.search(User, {"email": data.get("email")}):
        return jsonify({"msg": "Email already exists"}), 400

    try:
        new_instance = User(**data)
        new_instance.save()
        # Generate token
        token = new_instance.get_reset_token()
        return jsonify({"msg": "User created successfully",
                        "token": token}), 201
    except Exception as e:
        # Log the exception for debugging
        print(f"Error creating user: {e}")
        return jsonify({"msg": "Can't create User"}), 500


@auth_s.route("/login", methods=["POST"], strict_slashes=False)
@swag_from(login_swagger)
def login():
    """Login user"""
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    email = data.get("email")
    password = data.get("password")
    if not email:
        return jsonify({"msg": "Missing email"}), 400
    if not password:
        return jsonify({"msg": "Missing password"}), 400

    users = dbStorage.search(User, {"email": email})
    if not users:
        return jsonify({"msg": "User not found for this email"}), 404
    for user in users.values():
        if not user.is_validpassword(password):
            return jsonify({"msg": "Wrong password"}), 401

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        # save in database the token
        add_token_to_db(access_token)
        add_token_to_db(refresh_token)

        return {"access_token": access_token, "refresh_token": refresh_token}


@auth_s.route("/refresh", methods=["POST"], strict_slashes=False)
@jwt_required(refresh=True)
@swag_from(refresh_swagger)
def refresh():
    """refresh"""
    user_id = get_jwt_identity()  # user_id
    access_token = create_access_token(identity=user_id)
    # save access_token in database
    add_token_to_db(access_token)

    return {"access_token": access_token}, 200


@auth_s.route("/revoke_access", methods=["DELETE"], strict_slashes=False)
@jwt_required()
@swag_from(revoke_access_swagger)
def revoke_access_token():
    """revoke access token"""
    jti = get_jwt()["jti"]
    user_id = get_jwt_identity()
    revoke_token(jti, user_id)
    return {"msg": "Token revoked"}, 200


@auth_s.route("/revoke_refresh", methods=["DELETE"], strict_slashes=False)
@jwt_required(refresh=True)
@swag_from(revoke_refresh_swagger)
def revoke_refresh_token():
    """revoke refresh token"""
    jti = get_jwt()["jti"]
    user_id = get_jwt_identity()
    # acess  user
    user = get_current_user()
    revoke_token(jti, user_id)
    return {"msg": f"refresh token revoked from {user}"}, 200


@jwt.user_lookup_loader
def user_load(jwt_headers, jwt_payload):
    """load user from token"""
    user_id = jwt_payload[app.config["JWT_IDENTITY_CLAIM"]]
    return dbStorage.get(User, user_id)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_headers, jwt_payload):
    """check if token is revoked"""
    return is_token_revoked(jwt_payload)


@auth_s.route("/profile", methods=["GET"], strict_slashes=False)
@jwt_required()
@auth_role("Standard")
@swag_from(profile_swagger)
def get_user_profile():
    """get current user object"""
    current_user_id = get_jwt_identity()
    print(current_user_id)
    user = dbStorage.get(User, current_user_id)
    if not user:
        return {"msg": "User not found"}, 404
    return jsonify(user.to_json()), 200


def send_email(subject, sender, recipients, text_body, html_body):
    """send email"""
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail = Mail(app)
    try:
        mail.send(msg)
    except ConnectionRefusedError:
        raise InternalServerError("[MAIL SERVER] not working")


@auth_s.route("/forget_password", methods=["POST"], strict_slashes=False)
@swag_from(forget_password_swagger)
def send_reset_link():
    """requesting password reset link
    for users
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    email = data.get("email")
    if not email:
        return jsonify({"msg": "Missing email"}), 400

    all_users = dbStorage.all(User)
    users = [user for user in all_users.values() if user.email == email]
    if not users:
        return jsonify({"msg": "User not found"}), 401
    user = users[0]
    exps = datetime.timedelta(hours=2)
    reset_token = create_access_token(identity=user.id, expires_delta=exps)

    url = url_for("auth_s.reset_password")
    subject = "TuneTrackr Reset your Password"
    sender = "faustinemuhayemariya44@gmail.com"
    text_body = f"""Dear User,

    To reset your password, simply click the link below:

    {url}?reset_token={reset_token}

    If you haven't requested a password reset,
    you can safely ignore this message.

    Best regards,
    TuneTrackr Support Team
    """

    html_body = f"""<p>Dear User,</p>
    <p>To reset your password, simply
        <a href="{url}?reset_token={reset_token}">click here</a>.</p>
    <p>If you haven't requested a password reset,
        you can safely ignore this message.</p>
    <p>Best regards,<br>RepairRevoltHub Support Team</p>
    """

    send_email(
        subject,
        sender=sender,
        recipients=[user.email],
        text_body=text_body,
        html_body=html_body,
    )

    msg = f"Reset your password now: {url}?reset_token={reset_token}"

    # message = "A link to change to your password has been sent to your email"

    return jsonify({"email": msg})


@auth_s.route("/reset_password", methods=["PUT"], strict_slashes=False)
@swag_from(reset_password_swagger)
def reset_password():
    """change password when user has forgotten password"""

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    password = data.get("password")
    if not password:
        return jsonify({"msg": "Missing password"}), 400

    reset_token = request.args.get("reset_token")
    try:
        decoded_token = decode_token(reset_token)
        user_id = decoded_token.get("user_id")
    except Exception as e:
        return jsonify({"msg": f"Invalid token {str(e)}"}), 400

    user = dbStorage.get(User, user_id)
    if not user:
        return jsonify({"msg", "User not found"})
    for key, val in data.items():
        setattr(user, key, val)
    dbStorage.save()
    return jsonify({"msg": "Password changed successfully"})
