import os

path = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Zmienne_i_kod\test.txt'

os.remove(path) #kasowanie jeśli istnieje
'''
if os.path.isfile(path):
    print('Flile %s exists.' % path)
else:
    print('Creating %s file.' % path)
    open(path,'x').close() #tworzy plik, w czyli write, jakby plik istniał to byłby error i plik jest zamykany
    print('File %s created!' % path)
'''
'''
result = os.path.isfile(path) or open(path,'x').close() #<- często stosowane wyrażenie logiczne
print(result) #zwraca None ?! bo False i True w 2 warunku, zaś close zwróciło (a raczej nie zwróciło wartości i stąd None)
# , jakby plik istniał to byłoby True, bo nie sprawdził 2 warunku
'''
result = os.path.isfile(path) and open(path,'x').close() #koniunkcja czyli jak oba są True więc to spowoduje bład,
# a gdyby pliku nie było to będzie False, bo jak nie ma pliku to nie sprawdza dalej bo i tak będzie False i plik nie zostanie stworzony
print(result)






