items = input().split("|")
budget = float(input())

train_ticket = 150

sell_percentage = 1.4
sellings = 0
init_budget = budget
for el in items:
    item_args = el.split("->")
    item_type = item_args[0]
    item_price = float(item_args[1])
    
    if item_type == "Clothes" and (item_price < 0 or item_price > 50):
        continue
    elif item_type == "Shoes" and (item_price < 0 or item_price > 35):
        continue
    elif item_type == "Accessories" and (item_price < 0 or item_price > 20.5):
        continue
    
    if init_budget < item_price:
        continue
    
    item_for_sell = item_price * sell_percentage
    
    init_budget -= item_price
    sellings += item_for_sell
    
    print(f"{item_for_sell:.2f}", end = ' ')
    
print()
profit = sellings - (budget - init_budget)
print(f"Profit: {profit:.2f}")

income = sellings + (budget - init_budget)

if income > train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")