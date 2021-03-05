import itertools
import operator

# itertools.accumulate(iterable, func)

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)  # mul czyli multiplex - mnożenie
for each in result:
    print(each)

print('-' * 30)

data = [1, 2, 13, 4, 5]
result = itertools.accumulate(data, max)  # zwraca najwyższy natrafiony wynik
for each in result:
    print(each)

print('-' * 30)
for i in itertools.count(10, 3):  # podaje kolejne wartości, od ilu i co ile
    print(i)
    if i > 20:
        break

print('-' * 30)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# for m in itertools.cycle(months): #przechodzi przez zbiór w nieskończoność!!
# print(m)


print('-' * 30)
colors_basic = ['red', 'yellow', 'blue']
colors_mix = ['green', 'orange', 'violet']
result = itertools.chain(colors_basic, colors_mix)  # łączy obiekty iterable
for each in result:
    print(each)

print('-' * 30)
cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
selections = [True, False, True, False]
result = itertools.compress(cars, selections)
for each in result:
    print(each)

print('-' * 30)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.dropwhile(lambda x: x < 5, data) #opuszcza wartości do spełnionego warunku
for each in result:
    print(each)

print('-' * 30)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.filterfalse(lambda x: x < 5, data) #opuszcza wszystkie wartości niespełniające warunku
for each in result:
    print(each)

print('-' * 30)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
result = itertools.islice(months, 6, 8) #wyciąga wartości z listy od-do (ostatni nie jest brany pod uwagę)
for each in result:
    print(each)

print('-' * 30)
spades = ['Hearts','Tiles','Clovers','Pikes']
figures = ['Ace','King','Queen','Jack','10','9']
result = itertools.product(spades, figures) #dopasowanie 1:1 - iloczyn kartezjański
for each in result:
    print(each)

print('-' * 30)
for i in itertools.repeat('Tell me more', 5): #powtarza coś, ile razy
    print(i)

print('-' * 30)
data =[(1,2),(3,4),(5,6)]
result = itertools.starmap(operator.add, data) #operator względem danych i co ma się dziać
for each in result:
    print(each)

print('-' * 30)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.takewhile(lambda x: x < 5, data) #póki warunek prawdziwy to pobiera wartości
for each in result:
    print(each)

print('-' * 30)
cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
cars1, cars2 = itertools.tee(cars) # mirror, domyślne dwa
for each in cars1:
    print(each)

print('------')
for each in cars2:
    print(each)

print('-' * 30)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plan = ['busy', 'busy', 'busy', 'busy', 'busy', 'busy', 'free']
result = itertools.zip_longest(months, plan, fillvalue = 'unknown') #każdy z jednej poączyny jest z 2, zależnie od pozycji, jak nie ma dopasowania to fillvalue
for each in result:
    print(each)
