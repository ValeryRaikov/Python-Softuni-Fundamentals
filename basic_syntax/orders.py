number_of_orders = int(input())

total_price = 0
for _ in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    
    if price_capsule < 0.01 or price_capsule > 100:
        continue
    
    if days <= 0 or days > 31:
        continue
    
    if capsules_needed <= 0 or capsules_needed > 2000:
        continue
    
    order = price_capsule * days * capsules_needed
    print(f"The price for the coffee is: ${order:.2f}")
    total_price += order
    
print(f"Total: ${total_price:.2f}")