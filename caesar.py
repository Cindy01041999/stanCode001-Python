"""
File: caesar.py
Name: Chang Yen Yu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Define new version of alphabets, and create a formula 'deciphered(a,b)' to check the answer.
    """
    n = int(input('Secret number: '))
    s = input("What's the ciphered string? ")
    new_a = new_alphabet(n)
    replace_a = deciphered(s, new_a)
    print('The deciphered string is: ' + replace_a)


def new_alphabet(n):
    ans = ''
    part1 = ALPHABET[:26-n]
    part2 = ALPHABET[26-n:]
    ans = part2 + part1
    return ans


def deciphered(s, new_a):
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        door_number = new_a.find(ch)
        ans += ALPHABET[door_number]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
