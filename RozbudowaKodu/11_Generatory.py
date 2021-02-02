listA = list(range(6))
listB = list(range(6))

print(listA,listB)

product = []
for a in listA:
    for b in listB:
        product.append((a,b))
print(product)

#jednolinijkowiec
product = [(a,b) for a in listA for b in listB]
print(product)

#tylko parzyste z b i nieparzyste z listy a
product =[(a,b) for a in listA for b in listB if a % 2 == 1 and b% 2 ==0]
print(product)

#dla słowników tak samo
product ={a:b for a in listA for b in listB if a % 2 == 1 and b% 2 ==0}
print(product)

gen =((a,b) for a in listA for b in listB if a % 2 == 1 and b% 2 ==0)
print(gen)
#gen jest "programistyczny"
#używa się tam gdzie jest dużo (tysięcy) rekordów, ale szkoda pamięci

print(next(gen)) #zwraca pierszą wartość
print(next(gen)) #kolejny next pobiera kolejny
print('-'*30)
for x in gen: #pętlą for można wyświetlić komplet, prócz tych wyświetlonych przeze mnie wcześniej
    print(x)
print('-'*30)
for x in gen: #kolejny for nic nie daje, trzeba wykonać raz jeszcze generator
    print(x)

#przy ręcznym jak się skończą wygenerowane to będzie błąd
gen =((a,b) for a in listA for b in listB if a % 2 == 1 and b% 2 ==0)
print('*'*30)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all values have been generated')
        break


