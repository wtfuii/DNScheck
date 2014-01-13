import os
import string
import re

ALPHABET = list(string.ascii_lowercase)

def concreteiter(rounds, prestring = "", letters = ALPHABET):
    rounds -= 1
    if rounds >= 0:
        for letter in letters:
            prestring = prestring + letter
            if rounds == 0:
                response = str(os.popen('whois ' + prestring + '.com').read())
                #print(response)
                if re.match('No match for "', response):
                    print(prestring)
            concreteiter(rounds, prestring)
            prestring = prestring[:-1]

concreteiter(3)
