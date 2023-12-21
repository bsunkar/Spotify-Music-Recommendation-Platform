# Normal way
def trackDetails(item) -> dict:
    return {
        "id":str(item["_id"]),
        "track_id":item["track_id"],
        "artists":item["artists"],
        "album_name":item["album_name"],
        "track_name":item["track_name"],
        "popularity":item["popularity"],
        "duration_ms":item["duration_ms"],
        "explicit":item["explicit"],
        "danceability":item["danceability"],
        "energy":item["energy"],
        "key":item["key"],
        "loudness":item["loudness"],
        "mode":item["mode"],
        "speechiness":item["speechiness"],
        "acousticness":item["acousticness"],
        "instrumentalness":item["instrumentalness"],
        "liveness":item["liveness"],
        "valence":item["valence"],
        "tempo":item["tempo"],
        "time_signature":item["time_signature"],
        "track_genre":item["track_genre"]
    }

def tracksDetails(entity) -> list:
    return [trackDetails(item) for item in entity]
# #Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]