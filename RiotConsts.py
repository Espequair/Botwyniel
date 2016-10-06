URL = {
    "base": "https://{proxy}.api.pvp.net/api/lol/{region}/{url}",
    "summoner_by_name": "v{version}/summoner/by-name/{names}",
    "league": "v{version}/league/by-summoner/{summonerId}/entry",
    "current_game": "https://{proxy}.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}",
    "free_champions": "v1.2/champion",
    "statistics_summary": "v{version}/stats/by-summoner/{summoner_id}/summary"
}

API_VERSIONS = {
    "summoner": "1.4",
    "league": "2.5",
    "statistics": "1.3"
}

REGIONS = {
    "europe_west": "euw"
}

PLATFORM_IDS = {
    "euw": "EUW1",
    "br": "BR1",
    "eune": "EUN1",
    "kr": "KR",
    "lan": "LA1",
    "las": "LA2",
    "na": "NA1",
    "oce": "OC1",
    "tr": "TR1",
    "ru": "RU",
    "pbe": "PBE1",
    "jp": "JP"
}

CHAMPIONS_BY_ID = {
    1: 'Annie',
    2: 'Olaf',
    3: 'Galio',
    4: 'TwistedFate',
    5: 'XinZhao',
    6: 'Urgot',
    7: 'Leblanc',
    8: 'Vladimir',
    9: 'FiddleSticks',
    266: 'Aatrox',
    11: 'MasterYi',
    12: 'Alistar',
    13: 'Ryze',
    14: 'Sion',
    15: 'Sivir',
    16: 'Soraka',
    17: 'Teemo',
    18: 'Tristana',
    19: 'Warwick',
    20: 'Nunu',
    21: 'MissFortune',
    22: 'Ashe',
    23: 'Tryndamere',
    24: 'Jax',
    25: 'Morgana',
    26: 'Zilean',
    27: 'Singed',
    28: 'Evelynn',
    29: 'Twitch',
    30: 'Karthus',
    31: 'Chogath',
    32: 'Amumu',
    33: 'Rammus',
    34: 'Anivia',
    35: 'Shaco',
    36: 'DrMundo',
    37: 'Sona',
    38: 'Kassadin',
    39: 'Irelia',
    40: 'Janna',
    41: 'Gangplank',
    42: 'Corki',
    43: 'Karma',
    44: 'Taric',
    45: 'Veigar',
    48: 'Trundle',
    50: 'Swain',
    51: 'Caitlyn',
    53: 'Blitzcrank',
    54: 'Malphite',
    55: 'Katarina',
    56: 'Nocturne',
    57: 'Maokai',
    58: 'Renekton',
    59: 'JarvanIV',
    60: 'Elise',
    61: 'Orianna',
    62: 'MonkeyKing',
    63: 'Brand',
    64: 'LeeSin',
    267: 'Nami',
    68: 'Rumble',
    69: 'Cassiopeia',
    72: 'Skarner',
    268: 'Azir',
    74: 'Heimerdinger',
    75: 'Nasus',
    76: 'Nidalee',
    77: 'Udyr',
    78: 'Poppy',
    79: 'Gragas',
    80: 'Pantheon',
    81: 'Ezreal',
    82: 'Mordekaiser',
    83: 'Yorick',
    84: 'Akali',
    85: 'Kennen',
    86: 'Garen',
    89: 'Leona',
    90: 'Malzahar',
    91: 'Talon',
    92: 'Riven',
    96: 'KogMaw',
    98: 'Shen',
    99: 'Lux',
    101: 'Xerath',
    102: 'Shyvana',
    103: 'Ahri',
    104: 'Graves',
    105: 'Fizz',
    106: 'Volibear',
    107: 'Rengar',
    110: 'Varus',
    111: 'Nautilus',
    112: 'Viktor',
    113: 'Sejuani',
    114: 'Fiora',
    115: 'Ziggs',
    117: 'Lulu',
    119: 'Draven',
    120: 'Hecarim',
    121: 'Khazix',
    122: 'Darius',
    126: 'Jayce',
    127: 'Lissandra',
    131: 'Diana',
    133: 'Quinn',
    134: 'Syndra',
    143: 'Zyra',
    67: 'Vayne',
    150: 'Gnar',
    154: 'Zac',
    412: 'Thresh',
    157: 'Yasuo',
    161: 'Velkoz',
    421: 'RekSai',
    429: 'Kalista',
    432: 'Bard',
    201: 'Braum',
    203: 'Kindred',
    222: 'Jinx',
    223: 'TahmKench',
    236: 'Lucian',
    238: 'Zed',
    245: 'Ekko',
    10: 'Kayle',
    254: 'Vi',
    420: 'Illaoi',
    202: 'Jhin',
    136: 'Aurelion Sol',
    163: 'Taliyah',
    240: 'Kled',
    427: 'Ivern'
}

CHAMPION_IDS = [
    ['Orianna', 61],
    ['Skarner', 72],
    ['Gnar', 150],
    ['Swain', 50],
    ['Ashe', 22],
    ['Rammus', 33],
    ['Lux', 99],
    ['Varus', 110],
    ['LeeSin', 64],
    ['FiddleSticks', 9],
    ['Annie', 1],
    ['Leblanc', 7],
    ['Karma', 43],
    ['Kindred', 203],
    ['Braum', 201],
    ['Galio', 3],
    ['Zilean', 26],
    ['Zac', 154],
    ['Ryze', 13],
    ['Graves', 104],
    ['Alistar', 12],
    ['Katarina', 55],
    ['Bard', 432],
    ['Warwick', 19],
    ['Vladimir', 8],
    ['Brand', 63],
    ['Shyvana', 102],
    ['Rengar', 107],
    ['Sivir', 15],
    ['Yorick', 83],
    ['Amumu', 32],
    ['Malphite', 54],
    ['MasterYi', 11],
    ['Volibear', 106],
    ['Gragas', 79],
    ['Talon', 91],
    ['XinZhao', 5],
    ['Jinx', 222],
    ['Nunu', 20],
    ['Corki', 42],
    ['Khazix', 121],
    ['Mordekaiser', 82],
    ['Olaf', 2],
    ['Tryndamere', 23],
    ['Irelia', 39],
    ['Yasuo', 157],
    ['Morgana', 25],
    ['Singed', 27],
    ['Xerath', 101],
    ['Diana', 131],
    ['Teemo', 17],
    ['Shen', 98],
    ['Shaco', 35],
    ['Jax', 24],
    ['Kassadin', 38],
    ['Malzahar', 90],
    ['Nidalee', 76],
    ['Hecarim', 120],
    ['Evelynn', 28],
    ['Sion', 14],
    ['Caitlyn', 51],
    ['Aatrox', 266],
    ['Urgot', 6],
    ['Ahri', 103],
    ['Lucian', 236],
    ['Thresh', 412],
    ['Heimerdinger', 74],
    ['Kennen', 85],
    ['Lissandra', 127],
    ['Karthus', 30],
    ['Renekton', 58],
    ['Kalista', 429],
    ['Kayle', 10],
    ['TwistedFate', 4],
    ['Ezreal', 81],
    ['Nocturne', 56],
    ['KogMaw', 96],
    ['Cassiopeia', 69],
    ['Sejuani', 113],
    ['Nami', 267],
    ['Darius', 122],
    ['Akali', 84],
    ['Chogath', 31],
    ['Nautilus', 111],
    ['Anivia', 34],
    ['Vayne', 67],
    ['Velkoz', 161],
    ['Vi', 254],
    ['Taric', 44],
    ['Jayce', 126],
    ['Elise', 60],
    ['Fizz', 105],
    ['Rumble', 68],
    ['Ziggs', 115],
    ['Quinn', 133],
    ['Maokai', 57],
    ['JarvanIV', 59],
    ['Wukong', 62],
    ['Nasus', 75],
    ['MissFortune', 21],
    ['Lulu', 117],
    ['Viktor', 112],
    ['RekSai', 421],
    ['Poppy', 78],
    ['Udyr', 77],
    ['Tristana', 18],
    ['Azir', 268],
    ['DrMundo', 36],
    ['Sona', 37],
    ['Zyra', 143],
    ['Leona', 89],
    ['Janna', 40],
    ['Garen', 86],
    ['Syndra', 134],
    ['Soraka', 16],
    ['Gangplank', 41],
    ['Draven', 119],
    ['Zed', 238],
    ['Trundle', 48],
    ['Fiora', 114],
    ['Veigar', 45],
    ['Blitzcrank', 53],
    ['Twitch', 29],
    ['Ekko', 245],
    ['Riven', 92],
    ['Pantheon', 80],
    ['TahmKench', 223],
    ['Illaoi', 420],
    ['Jhin', 202],
    ['Aurelion Sol', 136],
    ['Taliyah', 163],
    ['Kled', 240],
    ['Ivern', 427]
]
