import time
import random
import os


# function pour netoiyer l'ecran
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def sequence_initiale():
    sequence = ""
    for i in range(4):
        chiffre = random.randint(0, 9)
        sequence += str(chiffre)

