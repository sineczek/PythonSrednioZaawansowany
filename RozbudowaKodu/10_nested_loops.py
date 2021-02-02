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
#{1: 4, 3: 4, 5: 4} bo identyfikacje są po kluczu, do klucza 1 najpier dodało :0 potem :2 i na końcu :4 i to zostało nadpisane










