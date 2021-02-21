import csv
import types

brandOnSale = 'Tesla'

def exportToFileStatic(path, header, data):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print('>>> This is function exportToFile - static method <<<') #czy metoda jest wywoływana - sprawdzanie

def exportToFileClass(cls,path):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print('>>> This is function exportToFile - class method <<<') #czy metoda jest wywoływana - sprawdzanie

def exportToFileInstance(self,path):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print('>>> This is function exportToFile - instance method <<<') #czy metoda jest wywoływana - sprawdzanie


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



print('--------- Static '*10)
Car.ExportToFileStatic = exportToFileStatic #dodanie funkcji do classy
#exportToFileStatic(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Klasy\lab_files\export_static.csv', ['Brand','Model','IsOnSale'], [car_01.brand, car_01.model, car_01.IsOnSale])
Car.ExportToFileStatic(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Klasy\lab_files\export_static.csv', ['Brand','Model','IsOnSale'], [car_01.brand, car_01.model, car_01.IsOnSale])

print('--------- Class '*10)
#Car.ExportToFileClass = exportToFileClass
Car.ExportToFileClass = types.MethodType(exportToFileClass, Car)
Car.ExportToFileClass(path=r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Klasy\lab_files\export_class.csv')

print('--------- Instance '*10)
#Car.ExportToFileInstance = exportToFileInstance()
car_01.ExportToFileInstance = types.MethodType(exportToFileInstance, car_01)
car_01.ExportToFileInstance(path=r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Klasy\lab_files\export_instance.csv')

print('-'*50)
if hasattr(car_01,'ExportToFileStatic') and callable(car_01.ExportToFileStatic):
    print('The object has method ExportToFileStatic')
if hasattr(car_01,'ExportToFileClass') and callable(car_01.ExportToFileClass):
    print('The object has method ExportToFileStatic')
if hasattr(car_01,'ExportToFileInstance') and callable(car_01.ExportToFileInstance):
    print('The object has method ExportToFileStatic')

