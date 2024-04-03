#!/usr/bin/env python3
from models.album import Album
from models.artist import Artist
from models import dbStorage
import pandas as pd
from datetime import datetime

data = [artist.to_json() for artist in dbStorage.all(Album).values()]
print(data)
# df = pd.DataFrame(data)
# print(df.to_string())
