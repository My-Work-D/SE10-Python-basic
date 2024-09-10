import random

def number_guessing_game():
    # Randomly select a number between 1 and 10
    number_to_guess = random.randint(1, 10)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    # Give the player 3 attempts to guess the number
    attempts = 3

    while attempts > 0:
        guess = int(input(f"\nYou have {attempts} attempts remaining. Enter your guess: "))

        if guess == number_to_guess:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        attempts -= 1

    # If the player runs out of attempts
    if attempts == 0:
        print(f"\nSorry, you've run out of attempts. The number was {number_to_guess}.")

# Run the game
number_guessing_game()
