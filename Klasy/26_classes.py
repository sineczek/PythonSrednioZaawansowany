#w drodze do klass

carBrand = 'BMW'
carModel = '320D (E91)'
carIsAirBagOK = True
carIsPaintingOK = True
carIsMechanicOK = True

def IsCarDamaged(carIsAirBagOK, carIsPaintingOK, carIsMechanicOK):
    return not (carIsAirBagOK and carIsPaintingOK and carIsMechanicOK)

print(IsCarDamaged(carIsAirBagOK, carIsPaintingOK, carIsMechanicOK))


def IsCarDamaged(carIsAirBagOK, carIsPaintingOK, carIsMechanicOK):
    return not (carIsAirBagOK and carIsPaintingOK and carIsMechanicOK)


car_01 = {
'carBrand' : 'BMW',
'carModel' : '320D (E91)',
'carIsAirBagOK' : True,
'carIsPaintingOK' : True,
'carIsMechanicOK' : True
}
car_02 = {
    'carBrand' : 'Tesla',
    'carModel' : 'S',
    'carIsAirBagOK' : True,
    'carIsPaintingOK' : False,
    'carIsMechanicOK' : True
}
print(IsCarDamaged(car_01['carIsAirBagOK'], car_01['carIsPaintingOK'], car_01['carIsMechanicOK']))

def IsCarDamaged(aCar):
    return not (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])



print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

cars = (car_01, car_02)
for c in cars:
    print("{} {} damaged = {}".format(c['carBrand'], c["carModel"], IsCarDamaged(c)))




