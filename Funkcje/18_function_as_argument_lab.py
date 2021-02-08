
'''Dane są następujące funkcje:

def double(x):
    return 2 *x

def root(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2
Napisz funkcję, która stanie się wspólnym interfejsem dla tych funkcji. Niech nowa funkcja nazywa sie generate_values i:

jako pierwszy argument przyjmuje nazwę funkcji (jedną z wyżej wymienionych)

jako drugi argument przyjmuje listę liczb, dla których ma być wyznaczona wartość

ta funkcja powinna wygenerować wartość dla każdej wartości z listy z poprzedniego punktu i zwrócić listę z wynikami

Przetestuj funkcję wywołując:

x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(root, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))
'''

def double(x):
    return 2 *x

def root(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

def generate_values(function, x_table):
    value_list = []
    for x in x_table:
        value_list.append(function(x))
    return value_list

x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(root, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))

