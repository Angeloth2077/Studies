def run():

    # Characters
    characters = {
        "Araxys": {
            "health": 700,
            "base_damage": 500,
            "armor": 100,
            "range": 50
        },
        "Luarn": {
            "health": 500,
            "base_damage": 400,
            "armor": 50,
            "range": 400
        },
        "Xorah": {
            "health": 600,
            "base_damage": 150,
            "armor": 200,
            "range": 200
        },
        "Roja": {
            "health": 900,
            "base_damage": 200,
            "armor": 500,
            "range": 100
        }
    }
    # Prints the stats of all characters
    for character, stat in characters.items():
        for stat, value in stat.items():
            print("\n" + character + " has " + str(value) + " " + stat)

if __name__ == "__main__":
    run()


