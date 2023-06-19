def find_perfect(number):
    divisors = []
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors.append(divisor)
            
    return sum(divisors) == number
            

number = int(input())          

if find_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")