CALORIES_PER_DAY = 2000

import re

pattern = r"(\||#)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{0,5})\1"

text = input()

matches = re.findall(pattern, text)

total_calories = 0
products = []
for match in matches:
    product = match[1]
    expiration_date = match[2]
    calories = int(match[3])
    
    products.append(f"Item: {product}, Best before: {expiration_date}, Nutrition: {calories}")
    
    total_calories += calories
    
food_days = total_calories // CALORIES_PER_DAY
print(f"You have food to last you for: {food_days} days!")

if products:
    print("\n".join(products))