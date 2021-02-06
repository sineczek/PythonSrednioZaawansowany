

def BuyMe(prefix = 'Please buy me', what = 'something nice', *args, **kwargs): #* oznacza że mamy listę, nazwa może być dowolna, zazwyczaj jednak to args,
    # kwargs - argument poprzedzony słowem kluczonym w słowniku {}
    print(prefix, what)
    (print(args))
    print(kwargs)

BuyMe('Please buy me','a new car.', 'a cat', 'a dog', 'a dragon', shop='market', color='any')

products = ['milk','bread','flakes']
parameters = {'price':'low', 'time':'now'}

BuyMe('Buy me', 'newspaper', *products, **parameters)








