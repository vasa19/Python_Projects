import random


def play():
    user = input(
        "What's you choice? 'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won"

    return "You lost"


def is_win(user, computer):
    if ((user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r')):
        return True


print(play())
