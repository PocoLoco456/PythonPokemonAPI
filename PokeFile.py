import api as pokeAPI


def openPokedex():
    try:
        file = open('Pokedex/pokemon.txt', 'r')
    except FileNotFoundError:
        file = createFile()
    return file


def getList():
    file = openPokedex()
    lines = file.read().splitlines()
    return lines


def isPokemon(pokemon):
    list = getList()
    return pokeAPI.isPokemon(list, pokemon)


def createFile():
    pokeFile = open("Pokedex/Pokemon.txt", "a+")
    pokeList = pokeAPI.listOfPokemon()
    for i in range(len(pokeList)):
        pokeFile.write(pokeList[i] + '\n')
    return pokeFile
