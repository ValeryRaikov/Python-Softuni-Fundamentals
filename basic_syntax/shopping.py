init_budget = int(input())

command = input()
while command != "End":
    product_price = int(command)
    
    if init_budget >= product_price:
        init_budget -= product_price
    else:
        print("You went in overdraft!")
        break
        
    command = input()
else:
    print("You bought everything needed.")