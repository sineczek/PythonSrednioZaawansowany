class Car:

    numberOfCars = 0 #zmienne na poziomie classy
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicalOK = isMechanicalOK
        Car.numberOfCars +=1
        Car.listOfCars.append(self)

    def IsDamged(self):
        return (self.isAirBagOK and self.isPaintingOK and self.isMechanicalOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print('Air Bag  - ok -           {}'.format(self.isAirBagOK))
        print('Painting - ok -           {}'.format(self.isPaintingOK))
        print('Mechanic - ok -           {}'.format(self.isMechanicalOK))
        print('-'*20)

print('Class level variables before creating instances: ', Car.numberOfCars, Car.listOfCars)

car_01 = Car('BMW', '320D (E91)', True, True, True) #instancje klasy
car_02 = Car('Tesla','Model S', True, False, True)

print('Class level variables after creating instances: ', Car.numberOfCars, Car.listOfCars)


print('ID of a class is: ', id(Car))
print('ID of instances are: ', id(car_01), id(car_02))

print('Check if object belongs to class using "isinstance": ', isinstance(car_01, Car)) #czy instancja powstała w oparciu o classę
print('Check if object belongs to class using "type": ', type(car_01) is Car) #czy instancja powstała w oparciu o classę
print('Check if object belongs to class using "__class__": ', car_01.__class__) #w oparciu o jaką classę powstała instancja

print('List of instances attributes with values using "vars": ', vars(car_01)) #pozwala zobaczyć jak zbudowany jest obiekt w formie słownika
print('List of class attributes with values using "vars": ', vars(Car)) #pozwala zobaczyć jak zbudowany jest classa w formie słownika

print('List of instances attributes with values using "dir": ', dir(car_01)) #kolejne metody dla instancji
print('List of class attributes with values using "dir": ', dir(Car)) #kolejne metody dla classy

print('Value taken from instance: ', car_01.numberOfCars, 'Value taken from class: ', Car.numberOfCars)
print('='*30)

