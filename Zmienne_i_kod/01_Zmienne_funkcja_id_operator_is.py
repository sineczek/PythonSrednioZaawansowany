myvar = 'Hello InteliJ!'
myvar2 = myvar+('!!')
print(myvar,myvar2)
print(type(myvar), type(myvar2))
print('Is value the same? ', myvar == myvar2) #False
print ('Are the variables the same? ',myvar is myvar2) #False
print(id(myvar),id(myvar2)) #id zmiennych, "adres w pamięci"
print('\n---------------')

myvar2 = myvar2[:-2]
print(myvar,myvar2)
print(type(myvar), type(myvar2))
print('Is value the same? ', myvar == myvar2) #True
print ('Are the variables the same? ',myvar is myvar2) #False
print(id(myvar),id(myvar2))

#zmienna wskazuje na obszar pamięci



