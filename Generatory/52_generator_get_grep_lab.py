'''W tym zadaniu napiszesz 2 generatory, które wykorzystasz do sprawdzenia adresów URL zapisanych w plikach w jednym
katalogu. Korzyść z takiego podejścia jest taka, że w programie osobno masz umieszczoną logikę pobierania nazw plików,
osobno czytania danych, osobno sprawdzania poprawności URL i wreszcie osobno jest część spinająca to wszystko razem.
Przy okazji - powtórka z korzystania z funkcji modułów os i requests. Do dzieła!

Zaimportuj moduły os i requests

Napisz generator  gen_get_files przyjmujący argument dir. Zadaniem generatora jest zwracać po kolei wszystkie pliki z
katalogu przekazanego jako parametr dir. (Skorzystaj z funkcji os.listdir(). Zwracaj pełną ścieżkę do pliku (skorzystaj
z os.path.join()
https://docs.python.org/3/library/os.html

Napisz generator gen_get_file_lines przyjmujący jako argument filename. Zadaniem generatora jest zwracać kolejne
linijki znajdujące się w pliku przekazanym jako parametr filename.  Zwracając wynik usuń z linijki potencjalny znak
enter występujący na końcu linii

Napisz funkcję check_webpage przyjmującą argument url.  Zadaniem funkcji jest pobranie strony określonej argumentem
url. (Pobierając stronę skorzystaj z requests. get(...)). Z funkcji zwróć wartość logiczną. Jeśli status zapisany w
wyniku wywołania funkcji response.get jest równy 200, to zwróć True. W przypadku innego statusu lub jakiegokolwiek
błędu zwróć False.

Korzystając z poniższego kodu utwórz podkatalog w katalogu c:/temp i w nim 2 pliki:

try:
    os.mkdir('c:/temp/links_to_check')
except:
    pass

with open('c:/temp/links_to_check/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('c:/temp/links_to_check/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')
Dla każdego pliku (file) zwracanego przez wywołanie generatora  gen_get_files('c:/temp/links_to_check')

oraz dla każdej  linijki (line) zwracanej przez wywołanie generatora gen_get_file_lines(file)

wywołaj funkcje check_webpage(line)

wyświetl na ekranie komunikat w postaci plik - adres www - True/False zależnie od tego czy adres jest poprawny czy nie'''
import os
import requests

try:
    os.mkdir(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\links_to_check')
except:
    pass

with open(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')


def gen_get_files(dir):
    for d in os.listdir(dir):
        yield os.path.join(dir, d)


def gen_get_file_lines(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            yield line.replace('\n', '')


def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

for file in gen_get_files(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\links_to_check'):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_webpage(line)))
