number = 10
print('Variable number: ', number, id(number))
number +=2
print('Variable number: ', number, id(number)) #inny id czyli inna zmienna, czyli jakby inna zmienna
#niezmienny fragment pamięcy czyli immutable!

text = 'Africa'
print('Variable text: ', text, id(text))
text += 'is hot'
print('Variable text: ', text, id(text))

#czyli zmienna jest niezmienna, zmienia się obszar w pamięci

list = [1, 2, 3]
print ('list', list, id(list))
list.append(4)
print ('list', list, id(list))
#listy są mutable czyli zmienne, bo id pozostaje bez zmian

list2 = list
print ('list2', list2, id(list2))
list2.append(5)
print ('list', list, id(list))
print ('list2', list2, id(list2)) #nadal te same zmienne
list3 = list.copy()
print ('list3', list3, id(list3))
list3.append(6)
print ('list', list, id(list))
print ('list3', list3, id(list3))



