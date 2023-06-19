import re

pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
dates = input()

results = re.finditer(pattern, dates)
for res in results:
    print(f"Day: {res.group('Day')}, Month: {res.group('Month')}, Year: {res.group('Year')}")