def run():


    # A list of characters    
    charactersHealth = {
        "Behemoth": 1000,
        "Araxys": 700,
        "Luram": 950,
        "Rehem": 850
    }

    #Prints all characters health aesthetically
    for character, HP in charactersHealth.items():
        if character == 'Behemoth':
            print("\n" + character + " has " + str(HP) + " HP points")
        elif HP == charactersHealth['Rehem']:
            print(character + " has " + str(HP) + " HP points" + "\n")
        else: 
            print(character + " has " + str(HP) + " HP points")



    #Print a specific character key based on the HP value
    for character, hp in charactersHealth.items():
        if hp == 1000:
            print(character)
        else: continue



if __name__ == '__main__':
    run()