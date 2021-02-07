def BuyMe(prefix='Please buy me', what='something nice'): #nazwy parametrów w (), jak jest = 'cos' to jest wartość domyślna
#jak 1wszy argument ma domyślną wartość to i kolejne muszą ją mieć
    print(prefix, what)

BuyMe('Please buy me','a new car.')
BuyMe(what = 'a new car.', prefix = 'Please buy me') #podając wartości można dowolną kolejność
BuyMe('Please buy me') #jak jest wartość domyślna określona w funkcji to można podać jeden argument, brakujący będzie z wartości domyślenj
BuyMe(prefix = 'Please buy me')
BuyMe(what='something sweet')



