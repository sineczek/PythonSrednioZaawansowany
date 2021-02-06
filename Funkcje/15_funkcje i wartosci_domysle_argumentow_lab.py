'''Napisz funkcję show_progress, która będzie wyświetlać linię tekstu powstałą wskutek powtórzenia zadaną ilość razy określonego znaku. Funkcja:

przyjmuje argument character, który określa jaki znak ma być powtarzany

przyjmuje argument how_many, który określa ile razy znak ma być powtórzony

wartość domyślna dla character to gwiazdka

Przetestuj działanie funkcji wywołując ją na różne sposoby np.:

show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')'''

def show_progress(how_many, character='*'):
    print(character*how_many)

'''z rozwiązania
def show_progress(how_many, character='*'):   
    line = character * how_many
    print(line)'''

show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')