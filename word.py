import csv
from random import *


def random_word():
    word_for_game = []
    with open("Эксперимент.csv", "r") as f:
        temp = csv.reader(f, delimiter=" ",)
        for i in temp:
            word_for_game.append(i)
    b = len(word_for_game)

    return "".join(word_for_game[randint(0, b)])
