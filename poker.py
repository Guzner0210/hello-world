import sys
import numpy as np


SUITS = ['h', 'd', 's', 'c']
NUMBERS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# CARDS = [(SUIT, NUMBER) for SUIT in SUITS for NUMBER in NUMBERS]

CARDS = []
for SUIT in SUITS:
    for NUMBER in NUMBERS:
        CARDS.append(SUIT+NUMBER)


def can_make_a_straight_pre_flop(c1, c2):
    def high_chance():
        print("There is a high chance that you can make a straight with this hand")

    def low_chance():
        print("There is a low chance that you can make a straight with this hand")

    if c1 in CARDS and c2 in CARDS :
        numbers = []
        for character in c1:
            numbers.append(character)
        for character in c2:
            numbers.append(character)

        if numbers[1] == '1' and numbers[4] == '1':
            low_chance()
        elif numbers[1] == '1' and numbers[4] == 'J':
            high_chance()
        elif numbers[1] == '1' and numbers[4] == 'Q':
            high_chance()
        elif numbers[1] == '1' and numbers[4] == 'K':
            high_chance()
        elif numbers[1] == '1' and numbers[4] == 'A':
            high_chance()
        elif numbers[1] == '1':
            if abs(10 - int(numbers[3])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[1] == 'J' and numbers[4] == '1':
            high_chance()
        elif numbers[1] == 'J' and numbers[3] == 'J':
            low_chance()
        elif numbers[1] == 'J' and numbers[3] == 'Q':
            high_chance()
        elif numbers[1] == 'J' and numbers[3] == 'K':
            high_chance()
        elif numbers[1] == 'J' and numbers[3] == 'A':
            high_chance()
        elif numbers[1] == 'J':
            if abs(11 - int(numbers[3])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[1] == 'Q' and numbers[4] == '1':
            high_chance()
        elif numbers[1] == 'Q' and numbers[3] == 'J':
            high_chance()
        elif numbers[1] == 'Q' and numbers[3] == 'Q':
            low_chance()
        elif numbers[1] == 'Q' and numbers[3] == 'K':
            high_chance()
        elif numbers[1] == 'Q' and numbers[3] == 'A':
            high_chance()
        elif numbers[1] == 'Q':
            if abs(12 - int(numbers[3])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[1] == 'K' and numbers[4] == '1':
            high_chance()
        elif numbers[1] == 'K' and numbers[3] == 'J':
            high_chance()
        elif numbers[1] == 'K' and numbers[3] == 'Q':
            high_chance()
        elif numbers[1] == 'K' and numbers[3] == 'K':
            low_chance()
        elif numbers[1] == 'K' and numbers[3] == 'A':
            high_chance()
        elif numbers[1] == 'K':
            if abs(13 - int(numbers[3])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[1] == 'A' and numbers[4] == '1':
            high_chance()
        elif numbers[1] == 'A' and numbers[3] == 'J':
            high_chance()
        elif numbers[1] == 'A' and numbers[3] == 'Q':
            high_chance()
        elif numbers[1] == 'A' and numbers[3] == 'K':
            high_chance()
        elif numbers[1] == 'A' and numbers[3] == 'A':
            low_chance()
        elif numbers[1] == 'A':
            if abs(14 - int(numbers[3])) >= 5 or abs(1 - int(numbers[3])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[4] == '1':
            if abs(10 - int(numbers[1])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[3] == 'J':
            if abs(11 - int(numbers[1])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[3] == 'Q':
            if abs(12 - int(numbers[1])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[3] == 'K':
            if abs(13 - int(numbers[1])) >= 5:
                low_chance()
            else:
                high_chance()
        elif numbers[3] == 'A':
            if abs(14 - int(numbers[1])) >= 5 or abs(1 - int(numbers[1])) >= 5:
                low_chance()
            else:
                high_chance()
        elif abs(int(numbers[1]) - int(numbers[3])) >= 5:
            low_chance()
        else:
            high_chance()
    else:
        print("Please enter the right syntax for cards")


def can_make_a_flush_pre_flop(c1, c2):
    def high_chance():
        print("There is a high chance that you can make a flush with this hand")

    def low_chance():
        print("There is a low chance that you can make a flush with this hand")

    if c1 in CARDS and c2 in CARDS :
        numbers = []
        for character in c1:
            numbers.append(character)
        for character in c2:
            numbers.append(character)

        if numbers[0] == numbers[2]:
            high_chance()
        else:
            low_chance()


def main():
    answer = input("Enter your cards? [Y/n] ")
    if answer == "y" or answer == "Y" or answer == "Yes" or answer == "YES":
        ans = True
        while ans:
            c1 = input("What is the first card? ")
            c2 = input("What is the second card? ")
            can_make_a_straight_pre_flop(c1, c2)
            can_make_a_flush_pre_flop(c1, c2)
            an = input("Do you wanna continue? [Y/n] ")
            if an == "y" or an == "Y" or an == "Yes" or an == "YES":
                continue
            else:
                break


# print(np.random.randint(1, 14, size=5))

if __name__ == '__main__':
    main()
    sys.exit()

