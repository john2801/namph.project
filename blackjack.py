import random
from replit import clear


def take_card():
    list_card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(list_card)


def cal_score(cal_cards):
    score = sum(cal_cards)
    if len(cal_cards) == 2 and score == 21:
        return 0
    else:
        if 11 in cal_cards and score > 21:
            cal_cards.remove(11)
            cal_cards.append(1)
            score = sum(cal_cards)
            return score
        else:
            return score
    if 11 in cal_cards and score > 21:
        cal_cards.remove(11)
        cal_cards.append(1)
        score = sum(cal_cards)
        return score


def compare_score(user_score, Comp_score):
    if Comp_score == 0 and user_score != 0:
        return "  Computer has a blackjack. YOu Lose 😭"
    if Comp_score != 0 and user_score == 0:
        return "  Your got a blackjack. You win 😎"
    if Comp_score > 21 and user_score <= 21:
        return "  You win 😎"
    if Comp_score <= 21 and user_score > 21:
        return "  You Lose 😭"
    if Comp_score > 21 and user_score > 21:
        return "  It's Draw 😎"
    if Comp_score > user_score:
        return "  You Lose 😭"
    if Comp_score < user_score:
        return "  You win 😎"
    if Comp_score == user_score:
        return "  It's Draw 😎"


def play_game():
    user_card = []
    comp_card = []
    for i in range(2):
        card = take_card()
        user_card.append(card)
        comp_card.append(card)
    comp_card.append(take_card())
    is_take_card = True
    while is_take_card:
        print(f"  Your card: {user_card}, Current Score: {cal_score(user_card)}")
        print(f"  Computer's first card: {comp_card[0]}")
        get = input("Type 'y' to get another card, type 'n' to pass: ")
        if get == "n":
            print(
                f"  Your final hand: {user_card}, final score : {cal_score(user_card)}"
            )
            is_take_card = False
        else:
            user_card.append(take_card())
            if cal_score(user_card) > 21:
                print(
                    f"  Your final hand: {user_card}, final score : {cal_score(user_card)}"
                )
                is_take_card = False
    while cal_score(comp_card) < 17 and cal_score(comp_card) != 0:
        comp_card.append(take_card())
    print(
        f"  Computer's Final Hand: {comp_card}, Computer's final Score: {cal_score(comp_card)}"
    )
    print(compare_score(cal_score(user_card), cal_score(comp_card)))
    another_game = input("Do you want to play a game of blackjack? Type 'y' or 'n'")
    if another_game == "y":
        clear()
        play_game()


play_game()
