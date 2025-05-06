import random 

def number_guessing_game():
    number = random.randint(1, 10)
    attempts = 0

    print("Guess the number between 1 and 10.")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess == number:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
            else:
                print("You are wrong. Try again.")
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()
