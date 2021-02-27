'''Zaczynamy od następującego kodu:

import requests
import os
import shutil

def save_url_to_file(url, file_path):

    r = requests.get(url, stream = True)
    with open(file_path, "wb") as f:
        f.write(r.content)

url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)
Napisz blok try/except/else/finally, który:

w bloku try

jeśli istnieje plik tmpfile_path to go usunie

korzystając z funkcji save_url_to_file pobierze stronę spod adresu url do pliku tmpfile_path

skopiuje plik tmpfile_path do file_path

w przypadku błędów wykonaj blok except, a w nim:

wyświetli informacje o błędzie, w tym szczegóły wyjątku

w bloku else  wyświetl komunikat o sukcesie

w bloku finally

usuń plik tmpfile_path jeśli istnieje

wyświetl komunikat

Przetestuj działanie programu z poprawnym i błędnym adresem url. Sprawdzaj wyniki wyświetlane na ekranie
'''


import requests
import os
import shutil

def save_url_to_file(url, file_path):

    r = requests.get(url, stream = True)
    with open(file_path, "wb") as f:
        f.write(r.content)

url = 'http://www.mobilo24.eu/spis/'
dir = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\ObsługaBłędów\lab_files'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)
try:
    if os.path.exists(tmpfile_path):
        print('Removing {}'.format(tmpfile_path))
        os.remove(tmpfile_path)

    print('Downloading url {}'.format(url))
    save_url_to_file(url, tmpfile_path)

    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)

except Exception as e:
    print('Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))

else:
    print('URL downloaded successfully {}'.format(file))

finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('DONE!')