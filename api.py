"""
Pokemon api

This file will be connecting to the pokemon api that is available at https://pokeapi.co/
This is an open source RESTful API. We will be using this to create profiles for specific Pokemon requested by the user.
The profiles will specify the pokemons type and which types cause the most damage to it (and vice versa)
"""

import requests as rq

# url to connect to the api for pokemon
url = 'https://pokeapi.co/api/v2/pokemon/'

# This url will be used to make a call for the types of pokemon can do the most damage
url1 = 'https://pokeapi.co/api/v2/type/'

# This url is used to make a call to obtain all pokemon. Should only be used once to create a local file
url2 = 'http://pokeapi.co/api/v2/pokemon/?limit=879'

# This will hold the name of the Pokemon who's information is being requested
pokemon = ''


# Retrieve the information of the specified pokemon
def getPokemon(pokemon):
    search = url + pokemon
    request = rq.get(search)
    return request.json()


# This will return the JSON of all pokemon in order of id
def getAllPokemon():
    search = url2
    request = rq.get(search)
    return request.json()


# Get all the pokemon and append them to a list. Return them, in order, alphabetically
def listOfPokemon():
    list = []
    allPokemon = getAllPokemon()
    for pokemon in allPokemon['results']:
        list.append(pokemon['name'])
    list.sort()
    return list


def getPokemonType(pokemon):
    # get dictionary associated with the pokemon type
    pokemonJSON = getPokemon(pokemon)
    types = pokemonJSON['types']
    type = types[0].get('type').get('name')
    return type


def getDamageRelation(pokeType):
    search = url1 + pokeType
    request = rq.get(search)
    return request.json()

# Could be made to return a dictionary and print from getInfo()
def getDamageTo(pokeType):
    # get dictionary associated with the damage type
    damageJSON = getDamageRelation(pokeType)
    relation = damageJSON['damage_relations']
    for damage in relation:
        print(damage)
        print('------------')
        for name in relation[damage]:
            if name.get('name') == ' ':
                print('None')
            else:
                print(name.get('name'))
        print('\n')


# This will get all the info for the related pokemon.
def getInfo(pokemon):
    type = getPokemonType(pokemon)
    print(pokemon.upper())
    print('-----------')
    getDamageTo(type)


# This will check if the string response given is a pokemon to search for. returns true or false. (this is a binary search)
def isPokemon(list, pokemon):
    first = 0
    last = len(list) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if list[mid] == pokemon:
            return True
        else:
            if pokemon < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False
