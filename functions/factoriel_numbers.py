def factoriel_first(a):
    factoriel = 1
    for num in range(1, a + 1):
        factoriel *= num
        
    return factoriel


def factoriel_second(a):
    factoriel = 1
    for num in range(1, a + 1):
        factoriel *= num
        
    return factoriel


def division_first_second(a, b):
    return f"{first_factoriel / second_factoriel:.2f}"

first = int(input())
second = int(input())

first_factoriel = factoriel_first(first)
second_factoriel = factoriel_second(second)

print(division_first_second(first_factoriel, second_factoriel))