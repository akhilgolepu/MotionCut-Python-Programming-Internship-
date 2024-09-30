from words import word_list
import random as ra

def valid_word(word_list):
    chosenword = ra.choice(word_list)
    
    while "-" in chosenword or " " in chosenword:
        chosenword = ra.choice(word_list)

    return chosenword.upper()
    
def hangman():
    chosenword = valid_word(word_list)
    attempts = len(chosenword) + 5
    dis = ["_" for letters in chosenword]

    while attempts>0 and "_" in dis:
        print("\n"+" ".join(dis))

        alphabet = input("Your guess?: ").upper()
        attempts -= 1

        if alphabet in chosenword:
            for index, letter in enumerate(chosenword):
                if alphabet == letter:
                    dis[index] = alphabet

            if attempts == 1:
                print(f"Right guess! {attempts} attempt remaining")
            else:
                print(f"Right guess! {attempts} attempts remaining")

        else:
            if attempts == 1:
                print(f"Wrong guess! {attempts} attempt remaining")
            else:
                print(f"Wrong guess! {attempts} attempts remaining")

    if "_" not in dis:
        print("You have successfully guessed the word!")
    else:
        print("You could not guess the word right! Try again")
        print("The word is ", chosenword)


print("Welcome to the Hangman game")
hangman()

command = input("Want to play command(y/n)?").lower()

if command == "y":
    hangman()
elif command == "n":
    exit()
else:
    print("Invalid choice")
