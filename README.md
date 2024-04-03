# tuneTrackr


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Api](#api)
- [Technologies Stack](#technologies-stack)
- [Author](#author)


## Overview
TuneTrackr is a music analytics web API service application that provides users with valuable insights into  music.
It use dataset from popular streaming services, analyzes them, identifies popular artists, tracks, album, and ranks top artists.
The Web Api offers comprehensive analytics and personalized recommendations for both music enthusiasts, artists and industry professionals.
[Short Video](https://youtu.be/q6Wbck6VJVA): show features for the Web API

## Features

Here are the features:

- User Account Management
- Discover Genres
- Explore Artists, Popular Artists,
- Browse Albums, Popular Albuma
- Search Tracks, Popular Tracks
- Find New Album Releases
- Similar Artists Suggestions
- Group Artists
- See Monthly Top Listened Artists
- Discover Top Tracks

## Architecture
![Architecture](https://github.com/faustine-van/tuneTrackr/assets/125466059/fae8492c-3f1a-458b-ae06-31a0f3cea8a3)

## TuneTrackr API

TuneTrackr API

### Files

### `tuneTrackr`

- `config.py`: configurations
- `exts.py`: extensions
- `generate_token.py`: function generate secret key


#### `models/`

- `base.py`: base of all models of the API - handle serialization
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
  1. First copy file name it `.env`
  	using this command `copy .env.shadow .env`
  2. add environment variables to it:

- How to get `JWT_SECRET_KEY` key

  1. run `python3 generate_token.py` and, then copy it
  2. add the key to `JWT_SECRET_KEY` in `.env` file

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

Genres Endpoints:

- `/genres (GET)`: Retrieve all genres.
- `/genres/genre_id` (GET): Retrieve a specific genre by its ID.
- `/genres/genre_id` (DELETE): Delete a genre by its ID.
- `/genres (POST)`: Create a new genre.
- `/genres/genre_id` (PUT): Update an existing genre.

Artists Endpoints:

- `/artists (GET):` Retrieve all artists.
- `/artists/artist_id` (GET): Retrieve a specific artist by its ID.
- `/artists/artist_id` (DELETE): Delete an artist by its ID.
- `/artists (POST)`: Create a new artist.
- `/artists/artist_id` (PUT): Update an existing artist.
Albums Endpoints:

- `/albums (GET)`: Retrieve all albums.
- `/albums/album_id` (GET): Retrieve a specific album by its ID.
- `/albums/album_id` (DELETE): Delete an album by its ID.
- `/albums (POST)`: Create a new album.
- `/albums/album_id` (PUT): Update an existing album.

Tracks Endpoints:

- `/tracks` (GET): Retrieve all tracks.
- `/tracks/track_id` (GET): Retrieve a specific track by its ID.
- `/tracks/track_id` (DELETE): Delete a track by its ID.
- `/tracks (POST)`: Create a new track.
- `/tracks/track_id` (PUT): Update an existing track.

Other Endpoints:

- `/new_albums` (POST): Retrieve new albums based on release date.
- `/similar_artists` (POST): Recommend similar artists.
- `/cluster_artists` (POST): Cluster artists based on attributes.
- `/top_artists` (POST): Retrieve most listened and followed artists.
- `/most_listened_artists` (POST): Retrieve most listened artists.
- `/popular_artists` (POST): Retrieve popular artists based on follower and popularity.

## Technologies Stack
![diagram-export-4-3-2024-10_10_51-AM](https://github.com/faustine-van/tuneTrackr/assets/125466059/caff3dfd-e3b4-4648-94c0-f2fada858eee)

## Author
- Email: [faustinemuhayemariya44@gmail.com]()

- Twitter: [faustine@van](https://twitter.com/44Fatech?s=09)

- LinkedIn: [LinkedIn](https://www.linkedin.com/in/muhayemariya-faustine-404376267?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
