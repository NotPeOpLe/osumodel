from enum import IntEnum, IntFlag

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


class TeamMode(IntEnum):
    score = 0
    accuracy = 1
    combo = 2
    scorev2 = 3


class ScoreMode(IntEnum):
    HeadToHead = 0
    TagCoOp = 1
    TeamVs = 2
    TagTeamVs = 3


class Mod(IntFlag):
    NoMod          = 0
    NoFail         = 1
    Easy           = 2
    TouchDevice    = 4
    Hidden         = 8
    HardRock       = 16
    SuddenDeath    = 32
    DoubleTime     = 64
    Relax          = 128
    HalfTime       = 256
    Nightcore      = 512        # Only set along with DoubleTime. i.e: NC only gives 576
    Flashlight     = 1024
    Autoplay       = 2048
    SpunOut        = 4096
    Relax2         = 8192       # Autopilot
    Perfect        = 16384      # Only set along with SuddenDeath. i.e: PF only gives 16416  
    Key4           = 32768
    Key5           = 65536
    Key6           = 131072
    Key7           = 262144
    Key8           = 524288
    FadeIn         = 1048576
    Random         = 2097152
    Cinema         = 4194304
    Target         = 8388608
    Key9           = 16777216
    KeyCoop        = 33554432
    Key1           = 67108864
    Key3           = 134217728
    Key2           = 268435456
    ScoreV2        = 536870912
    Mirror         = 1073741824
    KeyMod = Key1 | Key2 | Key3 | Key4 | Key5 | Key6 | Key7 | Key8 | Key9 | KeyCoop
    FreeModAllowed = NoFail | Easy | Hidden | HardRock | SuddenDeath | Flashlight | FadeIn | Relax | Relax2 | SpunOut | KeyMod
    ScoreIncreaseMods = Hidden | HardRock | DoubleTime | Flashlight | FadeIn