numbers = input().split(", ")
total_beggars = int(input())

beggars = [0] * total_beggars
for i in range(len(numbers)):
    beggar_index = i % total_beggars
    num = int(numbers[i])
    beggars[beggar_index] += num
    
print(beggars)