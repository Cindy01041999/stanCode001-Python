"""
File: complement.py
Name: Chang Yen Yu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Define build_complement(s) first, and then return values back to main().
    """
    print(build_complement('ATC'))
    print(build_complement(' '))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(s):
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        if ch == ' ':
            return 'DNA strand is missing.'
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'C':
            ans += 'G'
        elif ch == 'G':
            ans += 'C'
        else:
            ans = ans
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
