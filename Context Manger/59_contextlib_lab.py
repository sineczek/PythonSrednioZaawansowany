'''Przejrzyj klasę, która jest pewną modyfikacją klas z poprzednich zadań:

import os
import zipfile
import requests


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def close(self):
        if os.path.isfile(self.tmp_file):
            os.remove(self.tmp_file)

f = FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref1.zip')
f.download_file()

with zipfile.ZipFile(f.tmp_file, 'r') as z:
    a_file = z.namelist()[0]
    print(a_file)
    os.chdir('c:/temp')
    z.extract(a_file, '.', None)

    #os.remove(f.tmp_file)
Jak widać ta klasa nie jest context managerem, ale my to zmienimy:

zaimportuj moduł contextlib

zmień linijkę tworzącą instancję (f = FileFromWeb...) na instrukcję with tak, że do utworzenia context managera
wykorzystasz metodę closing z modułu contextlib

A teraz trochę popsujemy... :

w metodzie close zakomentuj wyrażenie if. Niech instrukcja usuwająca plik wykonuje się bezwarunkowo

uruchom kod - powinien działać poprawnie

odkomentuj ostatnią linijkę usuwającą plik. Uruchom ponownie skrypt, który tym razem powinien się kończyć błędem.

Naprawmy to:

Dodany w poprzednich krokach blok with umieść w kolejnym bloku with, który "ukryje" wyjątek FileNotFoundError

'''

import os
import zipfile
import requests
import contextlib


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def close(self):
        #if os.path.isfile(self.tmp_file):
        os.remove(self.tmp_file)

with contextlib.suppress(FileNotFoundError):

    with contextlib.closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Context Manger\lab_files\euroxref1.zip')) as f:

        f.download_file()

        with zipfile.ZipFile(f.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Context Manger\lab_files')
            z.extract(a_file, '.', None)

        os.remove(f.tmp_file)