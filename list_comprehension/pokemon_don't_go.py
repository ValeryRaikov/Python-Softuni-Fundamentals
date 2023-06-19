pokemons = [int(x) for x in input().split()]
removed_pokemons = []

def recalculate(pokemons_list):
    return[x + removed if x <= removed else x - removed for x in pokemons_list]

while pokemons:
    index = int(input())
    
    if index >= 0 and index <= len(pokemons):
        removed = pokemons.pop(index)
        removed_pokemons.append(removed)
        pokemons = recalculate(pokemons)
    elif index < 0:
        removed = pokemons.pop(0)
        pokemons.insert(0, pokemons[-1])
        removed_pokemons.append(removed)
        pokemons = recalculate(pokemons)
    elif index > len(pokemons):
        removed = pokemons.pop()
        pokemons.append(pokemons[0])
        removed_pokemons.append(removed)
        pokemons = recalculate(pokemons)
    
print(sum(pokemons))