import random

number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
attempts = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while (attempts<5):
    attempts += 1
    remaining_attempts=6-attempts    
    print(f"You have {remaining_attempts} attempts remaining to guess the number")
    guess = int(input("Enter your guess: "))
    if guess < number_to_guess:
        if attempts<5:
            print("Too low! Try again.")
        elif attempts==5:
            print("No more guesses... You loose! >_<")
    elif guess > number_to_guess:
        if attempts<5:
            print("Too high! Try again.")
        elif attempts==5:
            print("No more guesses... You loose! >_<")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break

print(f"The right guess was {number_to_guess}!!!!")
