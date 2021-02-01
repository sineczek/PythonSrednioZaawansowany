#QUIZ
#1.
numbers = list(range(1,10))

new_numbers = [x**2 for x in numbers]
print(new_numbers)

#2.
tie = ['green tie', 'gray tie', 'red tie']
shirt = ['white shirt', 'blue shirt', 'green shirt']

print(['I wear {} with {}'.format(t,s) for t in tie for s in shirt])

#3.
clients = ['A-company', 'B-company']
projects = [300,400,1500,2340,50]

investments = [(c,p) for c in clients for p in projects if c == 'A-company' and p < 1000 \
        or c =='B-company' and p >= 1000]
print(investments)

#wszystko udało się dobrze, tu tylko dla sprawdzenia :D

'''Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem otworzyć linie lotnicze 
"Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym

2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu

3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.

4. Policz ilość generowanych połączeń w krokach 1,2,3'''

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']


connections = [(a,b) for a in ports for b in ports]
print('Połączeń jest: {}'.format(len(connections)),'a połączenia to: ', connections)

connections = [(a,b) for a in ports for b in ports if a != b or b != a]
print('Połączeń jest: {}'.format(len(connections)),'a połączenia to: ', connections)

connections = [(a,b) for a in ports for b in ports if a < b]
print('Połączeń jest: {}'.format(len(connections)),'a połączenia to: ', connections)

#z rozwiązania
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [ (start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

routes = [ (start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))


routes = [ (start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))

