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
        print('-'*40)

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available on sale/promo')

    @classmethod #metoda na poziomie classy
    def ReadFromText(cls, aText): #cls to skrót od class
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    #metoda statyczna - może być wszędzie
    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW * 1.36

lineOfText = 'Renault:Megane:True:True:False:False'
car_03 = Car.ReadFromText(lineOfText)

car_01 = Car('BMW', '320D (E91)', True, True, True, False)
car_02 = Car('Tesla','Model S', True, False, True, True)

car_03.GetInfo()
print('converting 221KM to KW', Car.Convert_KM_KW(221))
print('converting 130KW to KM', Car.Convert_KW_KM(130))

print(car_03.ReadFromText(lineOfText))
print(car_03.Convert_KM_KW(50))











