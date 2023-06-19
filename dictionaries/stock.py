elements = input().split()

bakery = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = elements[i+1]
    bakery[product] = int(quantity)
    
check_for = input().split()
    
for prod in check_for:
    if prod in bakery.keys():
        print(f"We have {bakery[prod]} of {prod} left")
    else:
        print(f"Sorry, we don't have {prod}")