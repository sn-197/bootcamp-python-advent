# guess the number game

import random   

number_to_guess = random.randint(1, 20)

print("Welcome to the Guess the Number Game!")
print("I have picked a number from 1 up to 20.")

while True:
    guess = int(input("Enter your guess: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break