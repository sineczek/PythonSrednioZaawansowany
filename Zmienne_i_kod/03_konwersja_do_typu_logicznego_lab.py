'''Poniżej masz jedno zadanie - opisane mniej lub bardziej dokładnie - sam wybierz jaki opis preferujesz.
Rozwiązując zadanie staraj się, gdzie się da, korzystać z automatycznej konwersji do typu logicznego
(niezależnie od tego, czy to dobra praktyka czy nie)



Zadanie w wersji skróconej:

Napisz skrypt, który będzie wyświetlał użytkownikowi zestaw opcji do wyboru:

['load data', 'export data', 'analyze & predict']

Skrypt ma:

działać tak długo, aż użytkownik niczego nie wybierze i naciśnie enter

po wprowadzeniu wartości ma sprawdzać czy ta wartość jest liczbą

jeśli nie jest liczbą ma wyświetlić o tym komunikat

jeśli jest liczbą, to ma sprawdzić czy jest jednym z dopuszczalnych numerów opcji

jeśli tak, to ma wyświetlić komunikat z numerem wybranej opcji i treścią

jeśli nie, to ma wyświetlić komunikat o tym, że wybrana jest niepoprawna opcja





Zadanie w wersji nieco bardziej rozbudowanej:

Do zmiennej options wpisz listę dostępnych opcji ['load data', 'export data', 'analyze & predict']

Do zmiennej choice przypisz wartość 'x'

Napisz funkcję DisplayOptions, przyjmującą jako argument listę opcji która wyświetla komunikat w rodzaju:

1 - load data
2 - export data
3 - analyze & predict
Select option above or press enter to exit:
oraz pobiera wprowadzoną przez użytkownika wartość. Funkcja ma wczytać wartość i zwrócić ją jako string (bez jakiejkolwiek kontroli)

Napisz pętlę while, która działa tak długo, jak zmienna choice ma jakąś wartość

W tej pętli do zmiennej choice wczytuj wynik zwracany przez funkcję DisplayOptions

Napisz polecenie if/else, które sprawdza czy choice nie jest pustym napisem

jeśli tak:

w bloku try/except skonwertuj choice do liczby choice_num typu int

jeśli się udało

jeśli wartość jest dopuszczalna (większa od 0 i mniejsza równa od ilości opcji - wyświetl informacje o tym co zostało wybrane

jeśli wartość nie jest dopuszczalna, wyświetl komunikat o tym, że dokonano nieprawidłowego wyboru

jeśli się nie udało - wyświetl informację wskazującą na to że ma być wprowadzana liczba

Jeśli nie:

wyświetl informację o zakończeniu działania programu'''


choice='x'
options = ['load data', 'export data', 'analyze & predict']
def Options(options):
    for i in range(len(options)):
        print("{} - {}".format(i+1, options[i]))

    choice = input('Dokonaj wyboru lub wciśnij ENTER aby wyjść: ')
    return choice

while choice:

    choice = Options(options)

    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >=0 and choice_num < len(options):
                print('Wybrałeś {} - {}'.format(choice_num+1, options[choice_num]))
            else:
                print('Dokonaj wyboru (1-3) lub wciśnij ENTER aby wyjść')
        except:
            print('Miała być CYFRA!')
    else:
        print('----- FIN -----')