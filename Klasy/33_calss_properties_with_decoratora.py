brandOnSale = 'Tesla'

class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicalOK = isMechanicalOK
        self.__isOnSale = isOnSale

    @property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter #ustawiacz aby można było zmieniać poza
    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "Brand {}, Model {}".format(self.brand, self.model).title()


car_01 = Car('BMW', '320D (E91)', True, True, True, False)
car_02 = Car('Tesla','Model S', True, False, True, True)

print(car_01.IsOnSale)

del car_01.IsOnSale

print(car_01.IsOnSale)
print(car_01.CarTitle)










