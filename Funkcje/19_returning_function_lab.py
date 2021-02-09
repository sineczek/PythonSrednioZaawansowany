'''W tym zadaniu napiszesz funkcję, która będzie w stanie wygenerować 3 funkcje:

f_minutes - obliczającą różnicę między datami i wyrażającą ją w minutach

f_hours - obliczającą różnicę między datami i wyrażającą ją w godzinach

f_days - obliczającą różnicę między datami i wyrażającą ją w dniach

Jeśli już masz pomysł jak to zrobić, to działaj. Poniżej znajdują się bardziej szczegółowe instrukcje.

Oto 3 funkcje, które wykonują wspomniane operacje, ale zostały napisane ręcznie:

from datetime import datetime

def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]

def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]

def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]
Jak widać cała różnica jest w liczbie, którą należy podzielić duration_in_s. Są to:

60 dla minut

3600 dla godzin

86400 dla dni

Funkcje można przetestować w ten sposób:

start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))
Teraz przystąpisz do pisania swojej funkcji generującej inne funkcje:

1. Utwórz funkcję create_function przyjmującą argument span, który może przyjąć wartość:

'm' gdy należy wygenerować funkcję zwracającą różnicę w minutach

'h' gdy należy wygenerować funkcję zwracającą różnicę w minutach

'd' gdy należy wygenerować funkcję zwracającą różnicę w minutach

2. Zainicjuj zmienna sec odpowiednią dla span wartością liczbową, przez którą będziesz dzielił wartość w duration_in_s

3.  Do zmiennej tekstowej source wpisz tekst zawierający definicję dowolnej z początkowych funkcji, np. time_span_m

4. Zmień nazwę funkcji definiowanej w tekście source na f i zamień sztywną wartość liczbową na wartość ze zmiennej sec. Pamiętaj o usunięciu wcięć po lewej stronie - napis musi spełniać warunki formatowania dla Pythonowych funkcji.

5. Poleceniem exec wykonaj kod znajdujący się w zmiennej source. Pamiętaj o przekazaniu środowiska przy pomocy funkcji globals()

6. Zwróć funkcję f



Na tym etapie można sprawdzać efekty swojej pracy

1. Wygeneruj funkcje f_minutes wywołując create_function z parametrem 'm'

2. Wygeneruj funkcje f_hours wywołując create_function z parametrem 'h'

3. Wygeneruj funkcje f_days  wywołując create_function z parametrem 'd'

4. Przetestuj działanie funkcji:

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))
'''
from datetime import datetime

def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]

def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]

def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]



start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))


def create_function(span):

    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span =='d':
        sec = 86400

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(sec)

    exec(source, globals())

    return f

f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))

