'''Utwórz plik i wpisz do niego kilka słów, np co widzisz za oknem :)

Utwórz funkcję, która jako parametr przyjmuje ścieżkę dostępu do pliku i zwraca ilość słów w tym pliku, jeśli potrzebujesz kroków pomocniczych oto i one:

Otwórz plik poleceniem open (możesz skorzystać z parametru encoding="utf-16" jeżeli trzeba)

Wczytaj plik do zmiennej korzystając z funkcji read()

"Rozbij" wczytaną zawartość korzystając z funkcji split()

Policz ile elementów jest zwracanych przez funkcję split()

Zwróć tą wartość

W głównym skrypcie:

zadeklaruj zmienną path i przypisz jej wartość wskazującą na plik utworzony na początku

napisz polecenie warunkowe, które sprawdzi czy plik istnieje

jeśli tak, wywoła funkcję, policzy ilość słów w pliku i wyświetli o tym informację

napisz wyrażenie logiczne, które wykona te same czynności, co wcześniej napisana instrukcja if

'''

import os

path = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Zmienne_i_kod\testowy.txt'
def ilosc(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        iloscSlow = len(content.split())
    return iloscSlow

if os.path.isfile(path):
    print('Jest %d słów w pliku %s' % (ilosc(path), path))


os.path.isfile(path) and print('Jest {} słów w pliku {}'.format(ilosc(path),path))





