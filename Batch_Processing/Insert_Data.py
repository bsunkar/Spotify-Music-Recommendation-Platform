# importing libraries  
import pymongo
import pandas as pd
import json

# Connecting Mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")

# read spotify_tracks_genere csv file 

df = pd.read_csv("C:/Users/bsunkar/Desktop/BDS Assignment/data/train.csv")
# df.head(5)

data = df.to_dict(orient = "records")

db = client['spotifydb']

# Bulk Insert to mongodb (Batch Processing)
db.Tracks.insert_many(data)