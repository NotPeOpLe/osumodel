from ctypes import Union
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from httpx import AsyncClient, Response
from enums import GameMode, Genre, Language, Mod, RankStatus, ScoreMode, TeamMode
from settings import settings


class APIModel(BaseModel):
    __baseurl__: str = "https://osu.ppy.sh/api"
    __uri__: str = ""

    @classmethod
    async def get(cls, **params):
        async with AsyncClient() as client:
            respone: Response = await client.get(
                url=cls.__baseurl__ + cls.__uri__,
                params=dict(**params, k=settings.api_key)
            )
            respone.raise_for_status()
            result: Union[List[dict], dict] = respone.json()
            if isinstance(result, list):
                data_length: int = len(result)
                if data_length == 0:
                    return None
                if data_length > 1:
                    return [cls(**r) for r in result]
                return cls(**result[0])
            elif isinstance(result, dict):
                return cls(**result)
            else:
                raise TypeError(f"can't support type {type(result)}")


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


class ScoreBase(APIModel):
    user_id: int
    count100: int
    count300: int
    count50: int
    countgeki: int
    countkatu: int
    countmiss: int
    enabled_mods: Optional[Mod] = None
    maxcombo: int
    perfect: bool
    rank: str
    score: int

class Score(ScoreBase):
    __uri__ = "/get_scores"

    score_id: int
    username: str
    date: datetime
    pp: float
    replay_available: bool


class UserBest(ScoreBase):
    __uri__ = "/get_user_best"

    score_id: int
    beatmap_id: int
    date: datetime
    pp: float
    replay_available: bool


class UserRecent(ScoreBase):
    __uri__ = "/get_user_recent"

    beatmap_id: int
    date: datetime


class GameScore(ScoreBase):
    _pass: bool = Field(alias="pass")
    slot: int
    team: int


class MatchHeader(BaseModel):
    match_id: int
    name: str
    start_time: datetime
    end_time: Optional[datetime] = None


class MatchGame(BaseModel):
    game_id: int
    start_time: datetime
    end_time: datetime
    beatmap_id: int
    play_mode: GameMode
    match_type: int
    scoring_type: ScoreMode
    team_type: TeamMode
    mods: int
    scores: List[Score] = []


class Multiplayer(APIModel):
    __uri__ = "/get_match"

    match: Optional[MatchHeader] = 0
    games: List[MatchGame] = []


class Replay(APIModel):
    __uri__ = "/get_replay"

    content: str