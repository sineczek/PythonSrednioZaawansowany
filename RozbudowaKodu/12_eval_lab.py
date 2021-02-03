'''W tym zadaniu stworzysz mały kalkulator. Użytkownik wprowadzi wzór funkcji np.:

2*x

math.sin(x)

3*x**2+2*x-4

a program wyznaczy wartości tej funkcji dla x z przedziału (0,10) z dokładnością 0.1

1. Zaimportuj moduł math

2. Utwórz pustą listę argument_list

3. Napisz pętlę, która do listy argument_list doda

100 wartości

zaczynając od zera

gdzie każda kolejna jest o 0.1 większa od poprzedniej

4. Poproś użytkownika o wprowadzenie wzoru. Wzór zapisz w zmiennej formula. Użytkownik wprowadzając ten wzór powinien skorzystać ze zmiennej x do tego aby oznaczyć argument funkcji

5. Dla każdego elementu x z listy argument_list oblicz wartość funkcji wprowadzonej przez użytkownika i wyświetl jej wynik'''

import math
argument_list = []

for i in range(100):
    argument_list.append(i/10)

formula = input('Podaj wzór do obliczeń, użyj x do obliczeń: ')
for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))
