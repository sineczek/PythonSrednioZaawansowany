'''Oto funkcja pobierająca dane ze stron www:

import requests
import os


def save_url_file(url, dir, file,msg):

    print(msg.format(file))

    r = requests.get(url, stream = True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


Można ją wywołać korzystając z następującego kodu:



msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
dir = 'c:/temp/'
file = 'spis.html'
save_url_file(url, dir, file,msg)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'c:/temp/'
file = 'logo.png'
save_url_file(url, dir, file,msg)


Na potrzeby projektu, nad którym pracujesz katalog pobierania plików powinien zawsze być taki sam
(np. przyjmijmy c:\temp), a komunikat wyświetlany na ekranie powinien być zawsze "Please wait: {}"

Napisz funkcję partial  save_url_to_dir   która będzie mogła być wywoływana jedynie z argumentami dir i file'''

import requests
import os
import functools

def save_url_file(url, dir, file,msg):

    print(msg.format(file))

    r = requests.get(url, stream = True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)

msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
dir = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Funkcje - scenariusze zastosowań\lab_files'
file = 'spis.html'
save_url_file(url, dir, file,msg)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Funkcje - scenariusze zastosowań\lab_files'
file = 'logo.png'
#save_url_file(url, dir, file,msg)


save_url_to_dir = functools.partial(save_url_file, dir=r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Funkcje - scenariusze zastosowań\lab_files', msg = 'Please wait: {}')

save_url_to_dir(url = url, file = file)




