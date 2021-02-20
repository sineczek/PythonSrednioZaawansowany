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

car_01 = Car('BMW', '320D (E91)', True, True, True, False)
car_02 = Car('Tesla','Model S', True, False, True, True)

car_02.__isOnSale = False #jak dodaliśmy w classie __ to staje się "wewnętrzne",
#ale jak się zrobi tu _Car__isOnSale to się powiedzie

car_02.YearOfProduction = 2019 #dodanie atrybutu
del car_02.YearOfProduction #kasowanie atrybutu

setattr(car_02, 'TAXI', False) #dodawanie atrybuty
print(hasattr(car_02, 'TAXI')) #czy ma atrybut
delattr(car_02, 'TAXI')
print(hasattr(car_02, 'TAXI'))


car_02.GetInfo()




















