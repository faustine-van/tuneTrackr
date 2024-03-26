#!/usr/bin/python3
""" 3-main module """
import requests
from datetime import datetime
from models.genre import Genre
from models.album import Album
from models.artist import Artist
from models.track import Track

# Populate albums_ids and listeners lists with actual data
albums_ids = ["3KGVOGmIbinlrR97aFufGE", "18sR8zHx4zsVJUI4bHWuPC", "5Csjy4XeA7KnizkhIvI7y2",
              "6FJxoadUE4JNVwWHghBwnb", "0JGOiO34nwfUdDrD612dOp", "2bYCNZfxZrTUv1CHXkz2d2", "4KdtEKjY3Gi0mKiSdy96ML", "5DvJgsMLbaR1HmAI6VhfcQ"]
listeners = [30483051, 113488712, 88272066 , 72478581, 66506728, 53803391, 32160534, 68132353]

headers = {
    'Authorization': "Bearer BQAAgeFaW_wcOLUlc_3LfsPtZtT26Gr_OBKhQH9QjEC4T0w8M2fZfsWshBGofwVF1ActZkOrgt83o85VANhPIZp75eU1eOUs3h9P59U9TPuHdmWiKhQ"
}

for album_id, listener in zip(albums_ids, listeners):
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    res = requests.get(url, headers=headers)
    data = res.json()
    if data.get('error'):
        print(data.get('error'))
    print(data)
    title = data.get("name")
    popularity = data.get("popularity")
    label = data.get("label")
    release_date = data.get("release_date")
    total_tracks = data.get("total_tracks")
    artists_data = data.get("artists")
    url1 = artists_data[0].get('href')
    res1 = requests.get(url1, headers=headers)
    data1 = res1.json()

    genre_list = data1.get("genres")
    if len(genre_list) == 0 or not genre_list:
        print(f"No genres found for the album {title}. Skipping...")
        continue 
    genre_name = genre_list[0]
    # Add genre
    genre = Genre(name=genre_name)
    genre.save()

    followers = data1.get("followers").get("total")
    pop = data1.get("popularity")
    name = data1.get("name")
    # Add artist
    artist = Artist(name=name, follower=followers, popularity=pop,
                    genre_id=genre.id, monthly_listener=listener)
    artist.save()

    # Add album
    album = Album(title=title, release_date=datetime.strptime(release_date, "%Y-%m-%d"),
                    label=label, total_tracks=total_tracks, popularity=popularity, artist_id=artist.id)
    album.save()

    tracks = data.get('tracks').get("items")
    for track in tracks:
        url2 = track.get('href')
        res2 = requests.get(url2, headers=headers)
        data2 = res2.json()
        track_name = data2.get("name")
        track_pop = data2.get("popularity")
        track_position = data2.get("track_number")

        # Add track
        song = Track(name=track_name, artist_id=artist.id, album_id=album.id,
                        popularity=track_pop, track_position=track_position)
        song.save()
