for i in range(10,0,-1):
    print(i)

list = list(range(10))
print('List: ', list, type(list), id(list)) #klasa range, nie jest listą, jeśli nie będzie skonwertowana na list

list2=list[:] #też będzie nowyą listą
print('List2: ', list2, type(list2), id(list2))

print(list[5:7]) #jak zawsze ostatni jest pomijany, chyba że końca nie podamy
print(list[5:]) #5 do końća
print(list[:-1]) #do przedostatniego elementu
print(list[5:-1]) #od 5 do przedostatniego
print(list[:7:2]) #od pierwszego do 7 co 2 elementy
print(list[-1:0:-1]) #odwrócenie listy, co 1, bez elementu 0
print(list[-1::-1]) #od końca do samego początku

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
my_days = days[-2:]
print(my_days)

days = ['Monday','Tuesday','Wednesday','Thursday','Friday']

my_days = days[:]
my_days = my_days + ['Saturday', 'Sunday']

print(days[-2:-1])










