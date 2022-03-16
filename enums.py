from enum import IntEnum

class GameMode(IntEnum):
    osu = 0
    taiko = 1
    fruits = 2
    mania = 3

class RankStatus(IntEnum):
    graveyard = -2
    wip = -1
    pending = 0
    ranked = 1
    approved = 2
    qualified = 3
    loved = 4


class Genre(IntEnum):
    any = 0
    unspecified = 1
    video_game = 2
    anime = 3
    rock = 4
    pop = 5
    other = 6
    novelty = 7
    hip_hop = 9
    electronic = 10
    metal = 11
    classical = 12
    folk = 13
    jazz = 14


class Language(IntEnum):
    any = 0
    unspecified = 1
    english = 2
    japanese = 3
    chinese = 4
    instrumental = 5
    korean = 6
    french = 7
    german = 8
    swedish = 9
    spanish = 10
    italian = 11
    russian = 12
    polish = 13
    other = 14
