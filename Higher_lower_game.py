import art
from game_data import data
import random
from replit import clear

list_data = data


def pick_data():
    return random.choice(list_data)


def compare(a, b):
    if a["follower_count"] > b["follower_count"]:
        return a
    else:
        return b


def answer(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "A"
    else:
        return "B"


def play_game():
    object_a = pick_data()
    object_b = pick_data()
    is_true = True
    score = 0
    print(art.logo)
    while is_true:
        print(
            f"Compare A: {object_a['name']}, {object_a['description']}, {object_a['country']}"
        )
        print(art.vs)
        print(
            f"Against B: {object_b['name']}, {object_b['description']}, {object_b['country']}"
        )
        user_choose = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        if user_choose == answer(object_a, object_b):
            clear()
            print(art.logo)
            object_a = compare(object_a, object_b)
            object_b = pick_data()
            score = score + 1
            print(f"You're right! Current score: {score}")
        else:
            clear()
            print(art.logo)
            print(f"Sorry.That's wrong. Final score {score}")
            is_true = False
            play_again = input("Do you want to play another game? Type 'y' or 'n': ")
            if play_again == "y":
                clear()
                play_game()
            else:
                print("Good Bye. See Ya!")


play_game()
