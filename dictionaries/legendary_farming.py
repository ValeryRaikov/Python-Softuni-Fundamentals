legendary_products = {
    "shards": 0,
    "fragments": 0,
    "motes":0
}

junk_products = {}

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

obtained = False
while not obtained:
    materials = input().split()
    
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        product = materials[i+1].lower()
        
        if product in legendary_products:
            legendary_products[product] += quantity
            if legendary_products[product] >= 250:
                legendary_products[product] -= 250
                obtained = True
                print(f"{legendary_items[product]} obtained!")
                break
        else:
            if product in junk_products:
                junk_products[product] += quantity
            else:
                junk_products[product] = quantity
                
for prod, qnt in legendary_products.items():
    print(f"{prod}: {qnt}")
    
for prod, qnt in junk_products.items():
    print(f"{prod}: {qnt}")