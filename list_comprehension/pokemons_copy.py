pokemons = [int(x) for x in input().split()]
removed_list = []
 
 
def pokemon_recalculate(my_list):
    return [x + removed if x <= removed else x - removed for x in my_list]
 
 
while pokemons:
    idx = int(input())
 
    if 0 <= idx < len(pokemons):
        removed = pokemons.pop(idx)
        removed_list.append(removed)
        pokemons = pokemon_recalculate(pokemons)
 
    elif idx < 0:
        removed = pokemons.pop(0)
        fist_element = pokemons[-1]
        pokemons.insert(0, fist_element)
        removed_list.append(removed)
        pokemons = pokemon_recalculate(pokemons)
 
    else:
        removed = pokemons.pop()
        last_element = pokemons[0]
        pokemons.append(last_element)
        removed_list.append(removed)
        pokemons = pokemon_recalculate(pokemons)
 
print(sum(removed_list))