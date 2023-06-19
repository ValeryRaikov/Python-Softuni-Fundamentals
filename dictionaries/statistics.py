command = input()
bakery = {}

while command != "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)
    
    if product not in bakery.keys():
        bakery[product] = quantity
    else:
        bakery[product] += quantity
    
    command = input()
    
print("Products in stock:")
for product, quantity in bakery.items():
    print(f"- {product}: {quantity}")
    
print(f"Total Products: {len(bakery)}\nTotal Quantity: {sum(bakery.values())}")