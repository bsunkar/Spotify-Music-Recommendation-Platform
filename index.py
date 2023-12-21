from fastapi import FastAPI
# from routes.user import user 
from routes.tracks_genre import tracks_genere
app = FastAPI(title='Spotify Tracks Genere APIs')
# app.include_router(user)
app.include_router(tracks_genere)
# @app.get('/')
# def hello_world():
#     return{'hello':'world'}