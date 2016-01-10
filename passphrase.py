#!/usr/bin/python3
#
# Usage:
# ./passphrase.py <integer>
# The script will generate <integer> passphrases. If no integer is given, it will generate 10 passphrases.
# The wordlists included with this script were created by modifying the top 5000 most common words list from www.wordfrequency.info.
# The Noun and Verb lists are all singular; the Nouns and Verbs lists are all plural. This improves readability.
# In this first version only 6 patterns are implemented. Others might be devised. Be sure to remember to increase the middle number in the randrange() call if you add more.
# Enjoy!
#

from random import choice
from random import randrange
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

    pattern = randrange(1,7,1)

    if pattern == 1:
        files = ['Noun-common.list', 'Verbs-common.list', 'Adj-common.list', 'Nouns-common.list']
    elif pattern == 2:
        files = ['Noun-common.list', 'Verbs-common.list', 'Nouns-common.list', 'Adverb-common.list']
    elif pattern == 3:
        files = ['Adj-common.list', 'Nouns-common.list', 'Verb-common.list', 'Adverb-common.list']
    elif pattern == 4:
        files = ['Noun-common.list', 'Adverb-common.list', 'Verbs-common.list', 'Noun-common.list']
    elif pattern == 5:
        files = ['Noun-common.list', 'Adverb-common.list', 'Verbs-common.list', 'Nouns-common.list']
    elif pattern == 6:
        files = ['Noun-common.list', 'Verbs-common.list', 'Adverb-common.list', 'Adj-common.list']
    return files

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