import re

bought_items = []
pattern = r"^>>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)$"

total_money = 0
while True:
    line = input()
    if line == "Purchase":
        break

    result = re.findall(pattern, line)
    
    for res in result:
        item = res[0]
        price = float(res[1])
        quantity = int(res[3])

        bought_items.append(item)
        total_money += price * quantity
    
print("Bought furniture:")
for item in bought_items:
    print(item)
        
print(f"Total money spend: {total_money:.2f}")