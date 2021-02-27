brandOnSale = 'Tesla'

class Car:
    """
    Tu w komentrzy co to za klasa
    """
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale):
        """
        tu opis parametrow przekazywanych do metody init
        :param brand:
        :param model:
        :param isAirBagOK:
        :param isPaintingOK:
        :param isMechanicalOK:
        :param isOnSale:
        """

        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicalOK = isMechanicalOK
        self.__isOnSale = isOnSale

    @property
    def IsOnSale(self):
        """
        podobnie tu co się dzieje, co jest zwracane etc.
        :return:
        """
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

help(Car) #wyświetla informacje z komentarzy
help(Car.IsOnSale) #komentarz do metody









