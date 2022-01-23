# REPLIT VERSION
from replit import clear
from random import choice
from game_data import data
import art

pts = 0
a = choice(data)
data.remove(a)
b = choice(data)
data.remove(b)


def guess(opt):
    global end
    if a["follower_count"] > b["follower_count"]:
        answer = "A"
    else:
        answer = "B"
    if opt == answer:
        change()
        return score(1)
    else:
        end = True
        print(art.logo)
        return print(score(0))


def score(num):
    global pts
    if num == 1:
        pts += 1
    elif num == 0:
        return f"Sorry, that's wrong. Final score: {pts}"
    else:
        return f"You're right! Current score: {pts}"


def change():
    global a, b
    a = b
    b = choice(data)
    data.remove(b)


end = False


def game():
    while not end:
        print(art.logo)
        if pts > 0:
            print(score(3))
        print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")
        print(art.vs)
        print(f"Against B: {b['name']}, a {b['description']} from {b['country']}")
        opt = input("Who has more followers? Type 'A' or 'B': ").upper()
        clear()
        guess(opt)


game()
