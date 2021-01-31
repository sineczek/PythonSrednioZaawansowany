workDays = [ 19, 21, 22, 21, 20, 22]

print(workDays)

print(workDays[2]) #odwołanie sie do 3 elementu

enumeratedDays = list(enumerate(workDays)) #enumerate trzeba do listy, bo inaczej jest dramat - obiekt binarny
print(enumeratedDays)

for pos, value in enumeratedDays:
    print('Position: ', pos, 'value: ', value)

#zip łączy 2 niezależne listy

months = ['I','II','III','IV','V','VI']

monthsDays = list(zip(months, workDays)) #też obiekt binarny i dziwny wynik
print(monthsDays)

for m, d in monthsDays:
    print('Month',m,'Days',d)

for pos, (m,d) in enumerate(zip(months,workDays)):
    print('Position',pos,'month',m,'days',d)

#można łączyć więcej list z tą samą ilośćią danych


