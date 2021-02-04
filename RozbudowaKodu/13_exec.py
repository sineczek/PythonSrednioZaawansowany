var_x = 10
source = 'var_x = 2'

result = exec(source) #nie zwraca żadnej wartości, zawsze None
print(result)
print(var_x) #a zmodyfikował zmienną


var_x = 10
source = '''
new_var = 1
for i in range(var_x):
    print('-'* i)
    new_var += 1
'''

result = exec(source) #wykona pętle
print(result)
print(new_var)

#exec może przyjmowac również zmienne środowiskowe globals czy locals

source = input('Enter your expression: ')
print(eval(source)) #var_x * 333 to np. zostanie wykonane
print(exec(source))

