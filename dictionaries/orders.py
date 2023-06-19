products_by_quantity = {}
products_by_price = {}

command = input()
while command != "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    
    products_by_price[product] = price
    if product in products_by_quantity:
        products_by_quantity[product] += quantity
    else:
        products_by_quantity[product] = quantity
    
    command = input()
    
for product in products_by_quantity:
    price = products_by_price[product]
    quantity = products_by_quantity[product]
    total_price = price * quantity
    
    print(f"{product} -> {total_price:.2f}")