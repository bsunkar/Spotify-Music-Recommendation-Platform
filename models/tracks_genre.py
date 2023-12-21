from pydantic import BaseModel

class TracksGenere(BaseModel):
    track_id: str
    artists: str
    album_name: str
    track_name: str
    popularity: float
    duration_ms: int
    explicit: bool
    danceability: float
    energy: float
    key: int
    loudness: float
    mode: int
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    time_signature: int
    track_genre: str
