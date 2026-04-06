#number guessing game
import random
low=1
high=100
guess=0
number=random.randint(low,high)
while True:
    guess=int(input("enter ur guess:"))
    if guess>number:
        print(f"your guess is too high")
    elif guess<number:
        print(f"your guess is too low")
    else:
        print("your answer is correct")
        break
print("\n")
print(f"you take {guess}guessess")

