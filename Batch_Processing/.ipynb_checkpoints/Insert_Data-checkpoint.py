# importing libraries  
import pymongo
import pandas as pd
import json

# Connecting Mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")

# read spotify_tracks_genere csv file 

df = pd.read_csv("./data/train.csv")
df.head(5)