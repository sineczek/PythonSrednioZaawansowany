class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, accessories):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicalOK = isMechanicalOK
        Car.numberOfCars +=1
        Car.listOfCars.append(self)
        self.accessories = accessories


    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print('Air Bag  \t- ok -\t\t{}'.format(self.isAirBagOK))
        print('Painting \t- ok -\t\t{}'.format(self.isPaintingOK))
        print('Mechanic \t- ok -\t\t{}'.format(self.isMechanicalOK))
        print('Accessories\t\t\t\t{}'.format(self.accessories))
        print('-'*20)

    def __iadd__(self, other): #iadd to +=
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

car_01 = Car('BMW', '320D (E91)', True, True, True, ['winter rires'])
car_01.GetInfo()

car_01 +=['navi', 'roof rack']
car_01.GetInfo()

car_01 += 'loudspeeker system'
car_01.GetInfo()

car_02 = ['BMW', '330e (G20)', True, True, True, []]

car_pack = car_01 + car_02
print('car_01 + car_02 = ', car_pack[0].brand, car_pack[1].brand)
















