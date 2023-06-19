countries = input().split(", ")
capitals = input().split(", ")

country_dict = {countries[i]: capitals[i] for i in range(len(countries))}

for country, capital in country_dict.items():
    print(f"{country} -> {capital}")