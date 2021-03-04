import itertools as it

filepath = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\data.txt'

data = []

with open(filepath) as file:
    for line in file:
        elements = line.rstrip("\n").split(":")
        d = {'type': elements[0], 'action': elements[1]}
        data.append(d)

print(data)

#coś to nie działa jak na przykładzie
data = sorted(data, key = lambda x: x['type'])

for key, elements in it.groupby(data, key = lambda x: ['type']):
    print('The key is {} and the number of elements is {}'.format(key, len(list(elements))))








