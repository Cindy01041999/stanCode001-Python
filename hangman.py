"""
File: hangman.py
Name: Chang Yen Yu
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Create a new function to create a new word after user guess the alphabet.
    """
    r_word = random_word()
    b = build_word(r_word)  # build_word: "--------"
    print('The word looks like: ' + b)
    print('You have 7 wrong guesses left.')
    while True:
        ch = input('Your guess: ')  # ch: 猜的字
        i = r_word.find(ch)  # i:輸入的字ch是在第幾個位置　　＃r_word: 猜的字
        c = count(i)  # count(i): 7-n (n為猜第幾次)
        w = new_word(ch, i, r_word, b)
        b = w
        if i == -1:  # 這個字不存在
            print('There is no ' + ch + "'s in the word.")
        else:  # i != -1  # 這個字存在
            print('You are correct!')
        print('The word looks like: ' + w)
        print('You have ' + str(c) + ' wrong guesses left.')


def new_word(ch, i, r_word, b):
    # create a new word after guessing
    if i != -1:
        ans = ""
        for j in range(len(r_word)):
            if r_word[j] == ch:
                ans += ch
            elif b[j].isalpha():
                ans += b[j]
            else:
                ans += '-'
    return ans


def build_word(s):
    # the first word is "-------"
    t = ""
    for i in range(len(s)):
        t += "-"
    return t


def count(i):
    # the times left after guessing
    n = 0
    ans = N_TURNS - n
    if i != -1:
        n += 1
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
