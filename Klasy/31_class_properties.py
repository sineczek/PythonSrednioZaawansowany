brandOnSale = 'Tesla'

class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicalOK = isMechanicalOK
        Car.numberOfCars +=1
        Car.listOfCars.append(self)
        self.__isOnSale = isOnSale

    def IsDamged(self):
        return (self.isAirBagOK and self.isPaintingOK and self.isMechanicalOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print('Air Bag  \t- ok -\t\t{}'.format(self.isAirBagOK))
        print('Painting \t- ok -\t\t{}'.format(self.isPaintingOK))
        print('Mechanic \t- ok -\t\t{}'.format(self.isMechanicalOK))
        print('IS ON SALE\t\t\t\t{}'.format(self.__isOnSale))
        print('-'*20)

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available on sale/promo')


car_01 = Car('BMW', '320D (E91)', True, True, True, False)
car_02 = Car('Tesla','Model S', True, False, True, True)

'''print('Status of cars:', car_01.GetIsOnSale(), car_02.GetIsOnSale())
car_01.SetIsOnSale(True) #niepowinno się udać bo to nie Tesla - brandOnSale
car_02.SetIsOnSale(False) #powinno się udać bo to Tesla - brandOnSale
print('Status of cars:', car_01.GetIsOnSale(), car_02.GetIsOnSale())'''

#tu do właściwości się odwołuje, a nie do metody
car_01.IsOnSale(True)
car_02.IsOnSale(True)
print('Status of cars:', car_01.IsOnSale, car_02.IsOnSale)


















