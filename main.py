import api as pokeAPI
import PokeFile as pokeFile


def getUserInput(prompt):
    userInput = input(prompt)
    try:
        if isinstance(userInput, str):
            return userInput.lower()
        else:
            getUserInput('Enter a valid string')
    except:
        print('exception occurred')


if __name__ == '__main__':
    pokemon = getUserInput('Which pokemon will you be searching for?\n')
    while(pokeFile.isPokemon(pokemon) is False):
        pokemon = getUserInput('Enter a valid pokemon\n')
    pokeAPI.getInfo(pokemon)
