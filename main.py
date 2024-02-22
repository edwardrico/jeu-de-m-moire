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
        print(f"{sequence}\n")
        time.sleep(3)
        clear_screen()
        entree = input("Entrez la séquence:\n")
        if entree == sequence:
            print("Bravo, vous avez réussi \n")
            sequence += str(random.randint(0, 9))
            point += 1
        else:
            print(f"Vous avez perdu. Votre score est de {point} points et la séquence était {sequence}\n")
            break


if __name__ == "__main__":
    main()
