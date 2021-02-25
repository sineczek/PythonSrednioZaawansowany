brandOnSale = 'BMW'


class Car(object):
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale, accessories):
        print('>>This is __init__ of parent class:', self.__class__.__name__)

        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicalOK = isMechanicalOK
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)
        self.accessories = accessories

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isPaintingOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print('Air Bag  \t- ok -\t\t{}'.format(self.isAirBagOK))
        print('Painting \t- ok -\t\t{}'.format(self.isPaintingOK))
        print('Mechanic \t- ok -\t\t{}'.format(self.isMechanicalOK))
        print('IsOnSale \t- ok -\t\t{}'.format(self.__isOnSale))
        print('Accessories\t\t\t\t{}'.format(self.accessories))
        print('-' * 20)

    def __iadd__(self, other):  # iadd to +=
        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK,
                       self.isMechanicalOK, accessories)
        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK,
                       self.isMechanicalOK, accessories)
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def __add__(self, other):
        if type(other) is Car:
            return [self, other]
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def __str__(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model)

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale is valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'If set to TRUE, the car is available in sale/promo')


class Truck(Car):  # w nawiasie co ma być dziedziczone
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale, accessories, capacityKg):
        print('>>This is __init__ of child class:', self.__class__.__name__)
        super().__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale, accessories)
        # super(Truck, self) - czasem jest robione, nazwę klasy dla której się szuka rodzica, a potem instancję tej klasy
        # Car.__init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale)
        # można i tak, ale trzeba jawnie self przekazać, przydatne jak dziedziczy z kilku klas
        self.capacityKg = capacityKg

    def GetInfo(self):
        super().GetInfo()
        print('CapacityKg \t- ok -\t\t{}'.format(self.capacityKg))


truck_01 = Truck('Ford', 'Transit', True, False, True, False, [], 1600)
truck_02 = Truck('Renault', 'Trafic', True, True, True, True, [], 1200)

print('Calling properties:')
print(truck_01.brand, truck_01.capacityKg, truck_01.IsOnSale, truck_02.brand, truck_02.capacityKg, truck_02.IsOnSale)

truck_02.GetInfo()  # nie pokaże nowej cechy, bo wywołujemy na poziomie klasy car
truck_01.GetInfo()  # jak dodaliśmy getinfo do Truck to tylko tamto się wyświetli, chyba że dodamy super
