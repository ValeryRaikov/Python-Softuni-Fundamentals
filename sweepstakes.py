#Simple sweepstakes program to generate random numbers for the Bulgarian sweepstakes 6/49, 6/42, 5/35

from typing import List
from random import randint

START = 1

SWEEP_TYPES = {
    "5/35": (5, 35),
    "6/42": (6, 42),
    "6/49": (6, 49),
}

def sweepstakes(num_range: int, end_num: int) -> List:
    gen_nums = []
    
    for _ in range(num_range):
        while True:
            curr_num = randint(START, end_num)
            if curr_num in gen_nums:
                continue
            else:
                break
            
        gen_nums.append(curr_num)
        
    print(f"Random generated numbers are: ", end='')
    print(*sorted(gen_nums), end='')
    print(" Good luck!")
    
def generate_my_nums():
    while True:
        choice = input("Enter your sweepstakes type: ")
        try:
            sweepstakes(SWEEP_TYPES[choice][0], SWEEP_TYPES[choice][1])
            break
        except KeyError:
            print("Wrong sweep input! Enter again:")
    
while True:
    generate_my_nums()
    
    re_promt = input("Do you want to generate new numbers? ").lower()
    
    if re_promt == "no":
        break