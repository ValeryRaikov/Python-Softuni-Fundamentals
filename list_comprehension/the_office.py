happiness = input().split()
total_count = len(happiness)

happines_improvement = int(input())

new_happiness_levels = [int(hap) * happines_improvement for hap in happiness]

avg_happiness = sum(new_happiness_levels) / len(new_happiness_levels)

happy_people = len([person for person in new_happiness_levels if int(person) >= avg_happiness])

if happy_people >= total_count / 2:
    print(f"Score: {happy_people}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_people}/{total_count}. Employees are not happy!")