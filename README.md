# tuneTrackr


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Api](#api)
- [Future Enhancements](#future-enhancements)
- [Author](#author)


## Overview
TuneTrackr is a music analytics web API servcie application that provides users with valuable insights into the world of music.
It gathers data from popular streaming services such as YouTube and Spotify, analyzes trends, identifies popular genres, and ranks top artists.
The platform offers comprehensive analytics, personalized recommendations, and customizable reports for both music enthusiasts and industry professionals.



## Features


## TuneTrackr API

TuneTrackr API

### Files

### `tuneTrackr`

- `config.py`: configurations
- `exts.py`: extensions
- `generate_token.py`: function generate secret key


#### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model
- `auth.py`: auth model
- `storage/db.py`: database dbStorage model


#### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

- `auth/auth.py`: endpoints for authentication and authorization of the API
- `auth/helpers.py`: helper functions of the API
- `auth/decorators.py`: decorators for the API
- `auth/mail_service`: functions with mail service of the API



### Setup
First create `.env` file add environment variables folow:

```
# .env

# DATABASE and API
DB_USER
DB_PASS
DB_TUNETRACKR
DB_HOST
API_HOST 
API_PORT
DEBUG

# SECRECT KEY
JWT_SECRET_KEY

# variable for Gmail SMTP
MAIL_SERVER
MAIL_PORT
MAIL_USE_TLS
MAIL_USERNAME
MAIL_PASSWORD
MAIL_DEBUG
```

How to get `JWT_SECRET_KEY` key
  - run `python3 generate_token.py`
  - add the key to `JWT_SECRET_KEY` in `.env` file 

```
$ pip3 install -r requirements.txt
```



### Run

```
$ python3 -m api.v1.app
```


### Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

Endpoints handle various aspects of user authentication, registration, and password 
- `POST /auth/login`: User logs in with credentials.
- `POST /auth/register`: New user creates an account.
- `POST /auth/logout`: User logs out of their session.
- `POST /auth/profile`: User views their profile information.
- `POST /auth/refresh_token`: User refreshes their authentication token.
- `POST /auth/revoke_access`: User revokes access for a third-paPOST rty app.
- `POST /auth/revoke_refresh`: User revokes refresh token.
- `POST /auth/forget_password`: User initiates password reset.
- `POST /auth/reset_password`: User resets their password.



## Author
- Email: [faustinemuhayemariya44@gmail.com]()

- Twitter: [faustine@van](https://twitter.com/44Fatech?s=09)

- LinkedIn: [LinkedIn](https://www.linkedin.com/in/muhayemariya-faustine-404376267?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
