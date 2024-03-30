from models.album import Album
from models import dbStorage
import pandas as pd
from datetime import datetime

data = [album.to_json() for album in dbStorage.all(Album).values()]
print(data)
# df = pd.DataFrame(data)
# print(df.to_string())
