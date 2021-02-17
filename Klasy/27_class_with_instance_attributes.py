#programowanie proceduralne - niezleżne dane, funkcje etc.
#instancja klasy to obiekt
'''car_01 = {
    'carBrand': 'BMW',
    'carModel': '320D (E91)',
    'carIsAirBagOK': True,
    'carIsPaintingOK': True,
    'carIsMechanicOK': True
}
car_02 = {
    'carBrand': 'Tesla',
    'carModel': 'S',
    'carIsAirBagOK': True,
    'carIsPaintingOK': False,
    'carIsMechanicOK': True
}

def IsCarDamaged(aCar):
    return not (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])

print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

cars = (car_01, car_02)
for c in cars:
    print("{} {} damaged = {}".format(c['carBrand'], c["carModel"], IsCarDamaged(c)))
'''
print('-+'*30)

class Car:
#to jest szablon
#konstruktor - funckja uruchamina w momencie tworzenia instancji klsy - ma na celu utworzenie obiektu
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicalOK = isMechanicalOK
#instancje klasy
car_01 = Car('BMW', '320D (E91)', True, True, True)
car_02 = Car('Tesla','Model S', True, False, True)

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicalOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicalOK)




