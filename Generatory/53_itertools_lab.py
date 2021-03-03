'''Wyobraź sobie, że jesteś artystą szukającym natchnienia... Chcesz skomponować przebój, ale nie masz pomysłu jaki...

Do dyspozycji masz 7 nutek:

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
Główny motyw ma się składać z 4 nutek. Wyświetl wszystkie możliwe układy składające się z 4 nutek. Podpowiem, że na ile znam się na muzyce, kolejność nutek ma znaczenie. Skorzystaj z odpowiedniej funkcji z modułu itertools

Korzystając ze wzoru opisanego tutaj:

https://pl.wikipedia.org/wiki/Wariacja_bez_powt%C3%B3rze%C5%84

policz ile jest takich potencjalnych kandydatów na przebój.

'''

import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for x in it.permutations(notes, 4):
    print(x)

print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes))/math.factorial(len(notes) - 4)))

input('Press enter')

for x in it.product(notes, repeat=4):
    print(x)

print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
    pow(len(notes), 4)))

