from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator
from httpx import AsyncClient, Response
from enums import GameMode, Genre, Language, RankStatus
from settings import settings


class APIModel(BaseModel):
    __baseurl__: str = "https://osu.ppy.sh/api"
    __uri__: str = ""

    async def get(cls, **params):
        async with AsyncClient() as client:
            respone: Response = await client.get(
                url=cls.__baseurl__ + cls.__uri__,
                params=dict(**params, k=settings.api_key)
            )
            respone.raise_for_status()
            result: List[dict] = respone.json()
            data_length: int = len(result)
            if data_length == 0:
                return None
            if data_length > 1:
                return [cls(**r) for r in result]
            return cls(**result[0])


class Beatmap(APIModel):
    __uri__ = "/get_beatmaps"

    approved: RankStatus
    submit_date: datetime
    approved_date: datetime
    last_update: datetime
    artist: str
    beatmap_id: int
    beatmapset_id: int
    bpm: float
    creator: str
    creator_id: int
    difficultyrating: float
    diff_aim: float
    diff_speed:float
    diff_size: float
    diff_overall: float
    diff_approach: float
    diff_drain: float
    hit_length: int
    source: str
    genre_id: Genre
    language_id: Language
    title: str
    total_length: int
    version: str
    file_md5: str
    mode: GameMode
    tags: List[str] = []
    favourite_count: int
    rating: float
    playcount: int
    passcount: int
    count_normal: int
    count_slider: int
    count_spinner: int
    max_combo: int
    storyboard: bool
    video: bool
    download_unavailable: bool
    audio_unavailable: bool

    @validator("tags")
    def tags2list(value: str) -> List[str]:
        return value.split()

    @property
    def cover_url(self):
        return "https://assets.ppy.sh/beatmaps/" + self.beatmapset_id + "/covers/cover.jpg"

    @property
    def thumbnail_url(self):
        return "https://b.ppy.sh/thumb/" + self.beatmapset_id + "l.jpg"


class Event(BaseModel):
    display_html: str
    beatmap_id: int
    beatmapset_id: int
    date: datetime
    epicfactor: int


class User(APIModel):
    __uri__ = "/get_user"

    user_id: int
    username: str
    join_date: datetime
    count300: int
    count100: int
    count50: int
    playcount: int
    ranked_score: int
    total_score: int
    pp_rank: int
    level: float
    pp_raw: float
    accuracy: float
    count_rank_ss: int
    count_rank_ssh: int
    count_rank_s: int
    count_rank_sh: int
    count_rank_a: int
    country: str
    total_seconds_played: int
    pp_country_rank: int
    events: List[Event] = []

    @property
    def avatar_url(self):
        return "https://a.ppy.sh/" + self.user_id


class Score(APIModel):
    __uri__ = "/get_scores"

    score_id: Optional[int] = None
    score: int
    username: str
    count300: int
    count100: int
    count50: int
    countmiss: int
    maxcombo: int
    countkatu: int
    countgeki: int
    perfect: bool
    enabled_mods: int
    user_id: int
    date: datetime
    rank: str
    pp: Optional[float] = None
    replay_available: Optional[bool] = False


class UserBest(Score):
    __uri__ = "/get_user_best"

    beatmap_id: int


class UserRecent(UserBest):
    __uri__ = "/get_user_recent"