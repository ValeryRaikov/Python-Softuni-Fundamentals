cities = int(input())

total_money = 0
money_per_city = 0
for city in range(1, cities + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())
    
    profit = income - expenses
    
    money_per_city += profit
    
    if city % 3 == 0:
        money_per_city -= expenses * 0.5
        
    if city % 5 == 0:
        money_per_city -= income * 0.1
        
    if city % 3 == 0 and city % 5 == 0:
        money_per_city += expenses * 0.5
        
    print(f"In {city_name} Burger Bus earned {money_per_city:.2f} leva.")
    
    total_money += money_per_city
    money_per_city = 0
    
print(f"Burger Bus total profit: {total_money:.2f} leva.")