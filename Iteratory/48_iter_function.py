#aTuple = (1,2,3,4,5)

'''for x in aTuple:
    print(x)'''

'''#print(next(aTuple)) #nie da się
it = iter(aTuple)
print(next(it))
print(next(it))
print(next(it))
print(next(it))'''

'''aList = [1,2,3,4,5]

for i in aList:
    print(i)

#print(next(aList))
it = iter(aList)
print(next(it))
print(next(it))
print(next(it))
print(next(it))'''

'''aSet = [1,2,(3,4), 'another element',3,4]
#for i in aSet:
#    print(i)

#print(next(aSet)) #brak iteratora
it = iter(aSet)
print(next(it))
print(next(it))
print(next(it))'''

#zawartość pliku jest iterable
with open(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Iteratory\lab_files\testowy.txt','r') as file:
#    for line in file:
#        print(line)
    while True:
        try:
            print(next(file))
        except StopIteration:
            break

