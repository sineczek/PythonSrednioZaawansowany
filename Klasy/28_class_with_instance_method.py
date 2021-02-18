class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicalOK = isMechanicalOK

    def IsDamged(self):
        return (self.isAirBagOK and self.isPaintingOK and self.isMechanicalOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print('Air Bag  - ok -           {}'.format(self.isAirBagOK))
        print('Painting - ok -           {}'.format(self.isPaintingOK))
        print('Mechanic - ok -           {}'.format(self.isMechanicalOK))
        print('-'*20)

car_01 = Car('BMW', '320D (E91)', True, True, True)
car_02 = Car('Tesla','Model S', True, False, True)

print('='*30)

car_01.GetInfo()
car_02.GetInfo()

print(car_01.brand, car_01.model, car_01.IsDamged())
print(car_02.brand, car_02.model, car_02.IsDamged())

print('='*30)
print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicalOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicalOK)











