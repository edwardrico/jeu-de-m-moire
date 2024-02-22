import time
import random
import os


# Fonction pour nettoyer l'écran
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

    return sequence


def main():
    point = 0
    sequence = sequence_initiale()
    while True:
        print("Memorise la sequence ")
        print(sequence)
        time.sleep(3)
        clear_screen()
        entree = input("Quelle est la sequence : ")
        if entree == sequence:
            print("Bravo vous avez reusir")
            sequence += str(random.randint(0, 9))
            point += 1
        else:
            print(f" Vous avez perdu, vous cumulez {point} point et la sequence est {sequence}")
            break


if __name__ == "__main__":
    main()
