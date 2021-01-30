'''W tym zadaniu należy zapisać na dysku zawartość kilku stron www. Po zakończeniu pobierania należy wyświetlić komunikat o powodzeniu.
Jednak w przypadku błędu należy wyświetlić informację o błędzie i przerwać pętlę. Jeśli taki opis Ci wystarcza - do działa!

A oto opis "krok po kroku"
zaimportuj moduły os i urllib.request
w zmiennej data_dir zapisz ścieżkę do katalogu, w którym mają być zapisywane strony
w zmiennej pages zapisz informacje o stronach do pobrania. Może to być np. lista słowników:
pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]


dla każdej stony z pages:
zapisz w zmiennej path ścieżkę to pliku powstałą z połączenia data_dir, nazwy strony pobranej z  pages i ".html"

korzystając z  funkcji urllib.request.urlretrieve(<adres strony>, <sciezka do pliku>) zapisz stronę na dysku

(na tym etapie przetestuj sobie działanie programu)

wewnątrz pętli for dodaj blok try/except, który w przypadku błędu zakończy wykonywanie pętli, wyświetlając komunikat o błędzie

zakończ pętlę for poleceniem, które wykona się tylko wtedy gdy pętla nie została w żaden sposób przerwana. Wyświetl tu komunikat o powodzeniu'''

import os
import urllib.request

data_dir = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Zmienne_i_kod\doCwiczen'
pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    #{ 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:

    try:
        file_name = '{}.html'.format(page['name'])
        path = os.path.join(data_dir, file_name)

        print('Processing: {}  => {} ...'.format(page['url'], file_name))
        urllib.request.urlretrieve (page['url'], path)
        print('...done')

    except:
        print('FAILURE processing web page: {}'.format(page['name']))
        print('Stopping the process!')
        break

else:
    print('All pages downloaded successfully!!!')













