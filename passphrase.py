#!/usr/bin/python3
#
# Usage:
# ./passphrase.py <integer>
# The script will generate <integer> passphrases. If no integer is given, it will generate 10 passphrases.
# The wordlists included with this script were created by modifying the top 5000 most common words list from www.wordfrequency.info.
# The Noun and Verb lists are all singular; the Nouns and Verbs lists are all plural. This improves readability.
# In this version only 6 patterns are implemented. If you wish to add or remove a pattern, do so from the pattern= definition in pickpattern().
# Enjoy!
#

from random import choice
from sys import argv

def pickwords(filename):
    """This function chooses a random word from a chosen wordlist.
    :param filename: the wordlist that the function should search.
    :return: returns the randomly chosen word.
    """

    word = choice(open(filename, 'r').readlines()).rstrip('\r\n')
    return word


def pickpattern():
    """This function chooses the parts-of-speech pattern for the passphrase and returns the list"""

    pattern = [
        ['Noun-common.list', 'Verbs-common.list', 'Adj-common.list', 'Nouns-common.list'],
        ['Noun-common.list', 'Verbs-common.list', 'Nouns-common.list', 'Adverb-common.list'],
        ['Adj-common.list', 'Nouns-common.list', 'Verb-common.list', 'Adverb-common.list'],
        ['Noun-common.list', 'Adverb-common.list', 'Verbs-common.list', 'Noun-common.list'],
        ['Noun-common.list', 'Adverb-common.list', 'Verbs-common.list', 'Nouns-common.list'],
        ['Noun-common.list', 'Verbs-common.list', 'Adverb-common.list', 'Adj-common.list']
    ]

    return choice(pattern)


def main():
    """This is the main function of the script, which controls the number of passphrases created."""

    try:
        iterations = int(argv[1])
    except:
        iterations = 10

    for i in range(iterations):
        passphrase = ''
        files = pickpattern()

        for filename in files:
            word = pickwords(filename)
            passphrase += word

        print(passphrase)


if __name__ == '__main__':
    main()
