import random

def number_guessing_game():
    number_to_guess = random.ranint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("you are wrong,try again.")
            elif guess > number_to_guess:
                print("you are wrong. Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()
