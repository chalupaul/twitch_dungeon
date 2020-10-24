classes = [
    {
        "name": "Marine",
        "abilities": ["Regroup"],
        "weapons": ["M28", "Barretta 920"],
        "bonuses": {"str": 2, "con": 1},
    },
    {
        "name": "Medic",
        "abilities": ["Stim"],
        "weapons": ["Barretta 920", "Medkit"],
        "bonuses": {"con": 1, "wis": 2},
    },
    {
        "name": "Heavy Support",
        "abilities": ["Shield", "Cover Fire"],
        "weapons": ["XD4 Reaper"],
        "bonuses": {"int": 2, "dex": 1},
    },
    {
        "name": "Scout",
        "abilities": ["Survey", "Infiltrate"],
        "weapons": ["Barretta 920"],
        "bonuses": {"dex": 2, "int": 1},
    },
    {
        "name": "Hacker",
        "abilities": ["Spike"],
        "weapons": ["Dayll 3960x", "Barretta 920"],
        "bonuses": {"dex": 2, "wis": 1},
    },
    {
        "name": "Psionic",
        "abilities": ["Mind Blast", "Cloak", "Terrify"],
        "weapons": [],
        "bonuses": {"wis": 2, "dex": 1},
    },
]

weapons = [
    {"name": "M28", "desc": "Standard issue automatic rifle.", "damage": "2d8"},
    {"name": "Barretta 920", "desc": "8mm side arm pistol", "damage": "1d8"},
    {"name": "Medkit", "desc": "Bandages and gauze", "damage": "-1d8"},
    {
        "name": "XD4 Reaper",
        "desc": "A gatling cannon. Hits all enemies.",
        "damage": "1d8",
    },
    {
        "name": "Dayll 3960x",
        "desc": "A laptop with all the rootkits and password crackers you need",
        "damage": "0",
    },
]