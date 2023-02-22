LEVEL_EASY = 10
LEVEL_HARD = 5
import random
from replit import clear


def take_number():
    return random.randint(1, 100)


def guessing_process(difficulty):
    guessing_number = take_number()
    guessing_time = 1
    end_game = True
    while end_game:
        user_number = int(input("Making a guess: "))
        if difficulty <= guessing_time:
            print("You've run out of guess. You Lose.")
            break
        if user_number > guessing_number:
            print("Too high.")
            print(
                f"You have {difficulty-guessing_time} attempts remaining to guess the number."
            )
            print("Guess again.")
        if user_number < guessing_number:
            print("Too low.")
            print(
                f"You have {difficulty-guessing_time } attempts remaining to guess the number."
            )
            print("Guess again.")
        if user_number == guessing_number:
            print(f"You got it. The answer is {guessing_number}")
            end_game = False
        guessing_time = guessing_time + 1


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        print(f"You have {LEVEL_EASY} attempts remaining to get the number.")
        user_level = LEVEL_EASY
    else:
        print(f"You have {LEVEL_HARD} attempts remaining to get the number.")
        user_level = LEVEL_HARD
    guessing_process(difficulty=user_level)
    another_game = input("Do you want to guess another game? Type 'y' or 'n'.")
    if another_game == "y":
        clear()
        play_game()
    else:
        print("Bye. See Ya!")


play_game()
