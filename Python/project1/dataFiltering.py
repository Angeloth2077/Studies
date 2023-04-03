
characters = [
    {
        "name": "Araxys",
        "health": 400,
        "mele": True,
        "base_damage": 500,
        "role": "assassin",
        "armor": 100,
        "range": 50
    },
    {   
        "name": "Luarn",
        "health": 500,
        "mele": False,
        "base_damage": 400,
        "role": "shooter",
        "armor": 50,
        "range": 400
    },
    {   
        "name": "Xorah",
        "health": 600,
        "mele": False,
        "base_damage": 150,
        "role": "suport",
        "armor": 200,
        "range": 200
    },
    {  
        "name": "Roja",
        "health": 900,
        "mele": True,
        "base_damage": 200,
        "role": "tank",
        "armor": 500,
        "range": 100
    },
    {
        "name": "Nox",
        "health": 700,
        "mele": True,
        "base_damage": 250,
        "role": "fighter",
        "armor": 300,
        "range": 150
    }
]

def run():
    
    # meleChamps = [champ['name'] for champ in characters if champ['mele']]
    # nameOnly = list(map(lambda n: n['name'], tankyes))

    meleChamps = list(filter(lambda x: x['mele'] and x['range'] >= 100, characters))
    tankyes = list(map(lambda champ: champ | {'tanky': champ['armor'] > 100}, characters))

    for champ in tankyes:
        if champ['tanky']:
            print(champ['name'])

if __name__ == "__main__":
    run()