def orders(order, quantity):
    if order == "coffee":
        price = 1.5
    elif order == "coke":
        price = 1.4
    elif order == "water":
        price = 1
    elif order == "snacks":
        price = 2
        
    return f"{price * quantity:.2f}"

order = input()
quantity = int(input())
print(orders(order, quantity))