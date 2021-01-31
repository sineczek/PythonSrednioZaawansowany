'''Utwórz następujące listy:

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
Korzystając ze "sprytnej" metody pracy z for wyświetl komunikaty w postaci:

The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...



Utwórz kolejną listę z datami rozpoczęcia projektów:

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...'''

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for proj, lid in zip(projects,leaders):
    print('The leader of',proj,'is',lid)
    print('The leader of "{}" is {}'.format(p,l)) #z rozwiązania

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

projectsDatesLeaders = list(zip(projects,dates,leaders))
print(projectsDatesLeaders)

for p, l,d in zip(projects, leaders, dates):
    print('The leader of',p,'started',d,'is',l)
    print('The leader of "{}" started {} is {}'.format(p,d,l)) #z rozwiązania






