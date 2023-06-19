electrons = int(input())

n = 1
final = []
while electrons > 0:
    shell = 2 * (n**2)
    final.append(min(shell, electrons))
    
    n += 1
    electrons -= shell
    
print(final)