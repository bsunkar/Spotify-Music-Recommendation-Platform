from fastapi import HTTPException
from bson.errors import InvalidId
from fastapi import APIRouter
from models.tracks_genre import TracksGenere
# from models.user import User 
from config.db import conn 
# from schemas.user import usersEntity, userEntity ,serializeDict, serializeList
from schemas.tracks_genre import trackDetails, tracksDetails, serializeDict, serializeList
from bson import ObjectId
# user = APIRouter() 
tracks_genere = APIRouter()

@tracks_genere.get('/')
async def find_all_tracks():
    print(tracksDetails(conn.spotifydb.tracks_genere.find()))
    return tracksDetails(conn.spotifydb.tracks_genere.find())
    # return serializeList(conn.spotifydb.user.find())

# @tracks_genere.get('/{id}')
# async def find_one_track(id):
#     return serializeDict(conn.spotifydb.tracks_genere.find_one({"_id":ObjectId(id)}))

# @tracks_genere.get('/{id}')
# async def find_one_track(id: str):
#     # Try to find by _id first
#     track = conn.spotifydb.tracks_genere.find_one({"_id": ObjectId(id)})
#     if track is None:
#         # If not found, try to find by track_id
#         track = conn.spotifydb.tracks_genere.find_one({"track_id": id})
#     if track is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return serializeDict(track)

@tracks_genere.get('/{id}')
async def find_one_track(id: str):
    # Try to find by _id first
    try:
        track = conn.spotifydb.tracks_genere.find_one({"_id": ObjectId(id)})
    except InvalidId:
        # If not found or _id is invalid, try to find by track_id
        track = conn.spotifydb.tracks_genere.find_one({"track_id": id})
    if track is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return serializeDict(track)


@tracks_genere.post('/')
async def create_track(tracks_genere: TracksGenere):
    conn.spotifydb.tracks_genere.insert_one(dict(tracks_genere))
    return serializeList(conn.spotifydb.tracks_genere.find())

# @tracks_genere.put('/{id}')
# async def update_track(id,tracks_genere: TracksGenere):
#     conn.spotifydb.tracks_genere.find_one_and_update({"_id":ObjectId(id)},{
#         "$set":dict(tracks_genere)
#     })
#     return serializeDict(conn.spotifydb.tracks_genere.find_one({"_id":ObjectId(id)}))

# @tracks_genere.put('/{id}')
# async def update_track(id: str, tracks_genere: TracksGenere):
#     # Try to update by _id first
#     result = conn.spotifydb.tracks_genere.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(tracks_genere)})
#     if result is None:
#         # If not found, try to update by track_id
#         result = conn.spotifydb.tracks_genere.find_one_and_update({"track_id": id}, {"$set": dict(tracks_genere)})
#     if result is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return serializeDict(result)

@tracks_genere.put('/{id}')
async def update_track(id: str, tracks_genere: TracksGenere):
    # Try to update by _id first
    try:
        result = conn.spotifydb.tracks_genere.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(tracks_genere)})
    except InvalidId:
        result = None
    if result is None:
        # If not found or _id is invalid, try to update by track_id
        result = conn.spotifydb.tracks_genere.find_one_and_update({"track_id": id}, {"$set": dict(tracks_genere)})
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return serializeDict(result)

# @tracks_genere.delete('/{id}')
# async def delete_track(id,tracks_genere: TracksGenere):
#     return serializeDict(conn.spotifydb.tracks_genere.find_one_and_delete({"_id":ObjectId(id)}))

# @tracks_genere.delete('/{id}')
# async def delete_track(id: str):
#     # Try to delete by _id first
#     result = conn.spotifydb.tracks_genere.find_one_and_delete({"_id": ObjectId(id)})
#     if result is None:
#         # If not found, try to delete by track_id
#         result = conn.spotifydb.tracks_genere.find_one_and_delete({"track_id": id})
#     if result is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return serializeDict(result)

@tracks_genere.delete('/{id}')
async def delete_track(id: str):
    # Try to delete by _id first
    try:
        result = conn.spotifydb.tracks_genere.find_one_and_delete({"_id": ObjectId(id)})
    except InvalidId:
        result = None
    if result is None:
        # If not found or _id is invalid, try to delete by track_id
        result = conn.spotifydb.tracks_genere.find_one_and_delete({"track_id": id})
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return serializeDict(result)