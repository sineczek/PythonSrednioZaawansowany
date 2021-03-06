'''Oto klasa context managera z poprzedniego zadania:

import os
import zipfile
import requests

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        #download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:

    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)
Dodaj do tej klasy w __exit__ obsługę błędów:

jeśli w przedostatniej linijce zmieniasz katalog na nieistniejący, to zostanie wygenerowany błąd: FileNotFoundError
Należy tylko wyświetlić odpowiedni komunikat o błędzie (ukryć prawdziwą przyczynę)

jeśli w ostatniej linijce użytkownik poprosi o wypakowanie nieistniejącego pliku to zostanie wygenerowany błąd: KeyError
Należy tylko wyświetlić odpowiedni komunikat o błędzie (ukryć prawdziwą przyczynę)

w pozostałych przypadkach błąd ma być zgłoszony na zewnątrz

Uwaga! Jeśli do błędu dochodzi w metodzie __enter__, to pokazana na tej lekcji metoda nie zadziała, bo wtedy blok with
wcale się nie wykonuje, nie ma więc też metody __exit__'''

import os
import zipfile
import requests

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>>>>>>>>>> Error details',exc_type, exc_val, exc_tb)
        if exc_type == KeyError:
            print('>>>>> There is no file in archive! {}'.format(exc_val))
            return True
        elif exc_type == FileNotFoundError:
            print('>>>>> Incorrect directory/file: {}'.format(exc_val))
            return  True
        else:
            return False


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Context Manger\lab_files\euroxref.zip') as f:

    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Context Manger\lab_files')
        z.extract(a_file, '.', None)