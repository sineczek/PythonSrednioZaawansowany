#pozwala pobrać napis - fragment kodu - np. pobrać kod z bazy danych i np. wygenerować raport

var_x = 10
password = 'P@ssw0rd'

source = 'var_x + 2'
source = 'password' #ktoś może podać tu namiar na zmienną i wyświetli się tajne hasło

globals = globals().copy() #kopia zmiennych środowiskowych

resoult = eval(source, globals)
print(resoult)

#print(globals()) #zdefiniowane zmienne


globals = globals().copy() #kopia zmiennych środowiskowych
del globals['password'] #wykasowanie zmiennej password i przez to teraz kończy się błedem
#gdyż nie ma już dostępu do tej zmiennej password
resoult = eval(source, globals)
print(resoult)
print('-'*20)


source = '__import__("os").getcwd()'

globals = {} #puste środowisko

resoult = eval(source, globals)
print(resoult)




