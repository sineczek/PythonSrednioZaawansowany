class Car(object):

    def __init__(self, brand, model, isOnSale):
        print('>>Class Car - init - starting<<')
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = '{} {}'.format(brand, model)
        print('>>Class Car - init - stoping<<')

    def GetInfo(self):
        print('>>Class Car - GetInfo - starting<<')
        super().GetInfo() #gdyby tego nie było to mro - i nie szukłoby GetInfo w innych klasach rodziców
        print('{} {}'.format(self.brand, self.model).upper())
        print('IsOnSale \t- ok -\t\t{}'.format(self.isOnSale))
        print('>>Class Car - GetInfo - stoping<<')


class Specialist:

    def __init__(self, firstname, lastname, brand):
        print('>>Class Specialist - init - starting<<')
        self.firstname = firstname
        self.lastname = lastname
        self.name = '{} {}'.format(firstname, lastname)
        self.brand = brand
        print('>>Class Specialist - init - stoping<<')

    def GetInfo(self):
        print('>>Class Specilist - GetInfo - starting<<')
        print('{} {} - ({})'.format(self.firstname, self.lastname, self.brand).upper())
        print('>>Class Specialist - GetInfo - stoping<<')


class CarSpecialist(Car, Specialist):

    def __init__(self, brand, model, isOnSale, firstname, lastname):
        print('>>Class CarSpecialist - init - starting<<')
        Car.__init__(self,brand,model,isOnSale) #tak odwołuje się do większej ilości class, ale od self zaczynamy
        Specialist.__init__(self, firstname, lastname, brand.lower())
        print('>>Class CarSpecialist - init - stoping<<')

    def GetInfo(self):
        print('>>Class CarSpecilist - GetInfo - starting<<')
        super().GetInfo()
        print('>>Class CarSpecialist - GetInfo - stoping<<')



michal = CarSpecialist('BMW','320D (E91)', True, 'michal', 'sinq')
print(vars(michal))
michal.GetInfo()


#Method Resolution Order
print(CarSpecialist.__mro__)




