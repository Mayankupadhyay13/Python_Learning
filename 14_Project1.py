############## The Perfect Guess using Random Module #############

import random
n = random.randint(1,21)
inp = -1
guess = 0
while(inp != n):
    guess+=1
    inp = int(input('Guess the numbers: '))
    if(inp < n):
        print("Higher Number please...")
    elif(inp>n):
        print("Lower Number please ...")
    else:
        print(f"                        Congratulations!! : A PERFECT GUESS {n} in {guess} GUESSES")