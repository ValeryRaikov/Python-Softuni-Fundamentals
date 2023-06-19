MAX_MP = 200
MAX_HP = 100

heroes = {}

n = int(input())

for _ in range(n):
    command_args = input().split()
    hero_name = command_args[0]
    hp = int(command_args[1])
    mp = int(command_args[2])
    heroes[hero_name] = {"hp": hp, "mp": mp}
    
while True:
    line = input()
    if line == "End":
        break
    
    line_args = line.split(" - ")
    action = line_args[0]
    hero_name = line_args[1]
    if action == "CastSpell":
        mp_needed = int(line_args[2])
        spell = line_args[3]
        if heroes[hero_name]["mp"] >= mp_needed:
            heroes[hero_name]["mp"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")
    elif action == "TakeDamage":
        damage = int(line_args[2])
        attacker = line_args[3]
        heroes[hero_name]["hp"] -= damage
        if heroes[hero_name]["hp"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif action == "Recharge":
        amount = int(line_args[2])
        old_mp = heroes[hero_name]["mp"]
        heroes[hero_name]["mp"] = min(MAX_MP, heroes[hero_name]["mp"] + amount)
        if heroes[hero_name]["mp"] < 200:
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            print(f"{hero_name} recharged for {MAX_MP - old_mp} MP!")
    else:
        amount = int(line_args[2])
        old_hp = heroes[hero_name]["hp"]
        heroes[hero_name]["hp"] = min(MAX_HP, heroes[hero_name]["hp"] + amount)
        if heroes[hero_name]["hp"] < 100:
            print(f"{hero_name} healed for {amount} HP!")
        else:
            print(f"{hero_name} healed for {MAX_HP - old_hp} HP!")
        
for hero, hero_info in heroes.items():
    print(f"{hero}\n  HP: {hero_info['hp']}\n  MP: {hero_info['mp']}")
