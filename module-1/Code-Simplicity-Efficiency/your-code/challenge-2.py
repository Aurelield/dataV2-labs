"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random
import sys
import string

def RandomStringGenerator(l):
    return ''.join([random.choice(string.ascii_lowercase + string.digits) for i in range(l)])

def BatchStringGenerator(n, m=8, M=12):
    # n = argument positionnel = argument obligatoirement indiqué lors de l'appel de la fonction
    # et dont l'ordre (ou la position) est fixe
    # m, M = arguments optionnels (keyword arguments) = arguments facultativement indiqués lors de l'appel
    # de la fonction, et s'ils ne sont pas précisés, ils prennent alors une valeur par défaut qui est celle
    # indiquée après le "=". De plus leur ordre / position n'est pas important
    if m > M:
        raise ValueError('Incorrect min and max string lengths. Try again.')
    return [RandomStringGenerator(m) if m == M 
            else RandomStringGenerator(random.choice(range(m, M))) for i in range(n)]

m = input('Enter minimum string length: ')
M = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(m), int(M)))
