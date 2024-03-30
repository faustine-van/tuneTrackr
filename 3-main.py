#!/usr/bin/python3
""" 3-main module """
import requests
from datetime import datetime
from models.genre import Genre
from models.album import Album
from models.artist import Artist
from models.track import Track

# Populate albums_ids and listeners lists with actual data
albums_ids = [
    "5r36AJ6VOJtp00oxSkBZ5h",
    "0gY9Z6WFEkZgFFalIG0cc6",
    "5PKl5yyetQ6mFeWK6ONbSH",
    "6Hawd2zlOPgisX0Gx4ApPN",
]
listeners = [58252148, 29386636, 16220460, 8907265]

headers = {
    "Authorization": "Bearer BQD9Nxb1xAkLeXWmN7B4GTApM3uA8QwlWs0GIBznSgOQkoRncq_IwBk7URWf0tHbFrS8-Lc_8LW62yKp2llTeWfDYSLI9OK5zHPec4f5JfeXXuCrAY8"
}

for album_id, listener in zip(albums_ids, listeners):
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    res = requests.get(url, headers=headers)
    data = res.json()
    if data.get("error"):
        print(data.get("error"))
    title = data.get("name")
    popularity = data.get("popularity")
    label = data.get("label")
    release_date = data.get("release_date")
    total_tracks = data.get("total_tracks")
    artists_data = data.get("artists")
    url1 = artists_data[0].get("href")
    res1 = requests.get(url1, headers=headers)
    data1 = res1.json()

    genre_name = None
    genre = None
    genre_list = data1.get("genres")
    if genre_list is not None and len(genre_list) > 0:
        genre_name = genre_list[0]

    # Assuming Genre class has a save method
    if genre_name is not None:
        genre = Genre(name=genre_name)
        genre.save()

    followers = data1.get("followers").get("total")
    pop = data1.get("popularity")
    name = data1.get("name")
    genre_id = None if genre is None else genre.id
    # Add artist
    artist = Artist(
        name=name,
        follower=followers,
        popularity=pop,
        genre_id=genre_id,
        monthly_listener=listener,
    )
    artist.save()

    # Add album
    album = Album(
        title=title,
        release_date=datetime.strptime(release_date, "%Y-%m-%d"),
        label=label,
        total_tracks=total_tracks,
        popularity=popularity,
        artist_id=artist.id,
    )
    album.save()

    tracks = data.get("tracks").get("items")
    for track in tracks:
        url2 = track.get("href")
        res2 = requests.get(url2, headers=headers)
        data2 = res2.json()
        track_name = data2.get("name")
        track_pop = data2.get("popularity")
        track_position = data2.get("track_number")

        # Add track
        song = Track(
            name=track_name,
            artist_id=artist.id,
            album_id=album.id,
            popularity=track_pop,
            track_position=track_position,
        )
        song.save()
