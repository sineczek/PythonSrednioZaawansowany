workDays = [ 19, 21, 22, 21, 20, 22]
months = ['I','II','III','IV','V','VI']

monthsDays = dict(zip(months,workDays)) #powstał słownik
print(monthsDays)


'''
przy takim zapisie pojawi się bład: not enough values to unpack (expected 2, got 1)
z uwagi na to, że element monthsDays składa się z jednego pola {xx:xx}
for key,value in monthsDays: 
    print('Key is',key,'value is', value)
'''

for key in monthsDays:
    print('Key is',key,'value is', monthsDays[key])

#lepiej list, bo w starszych pythonah nie koniecznie wartości będę zwrócone w kolejności
for value in monthsDays.values():
    print('the value is',value)


