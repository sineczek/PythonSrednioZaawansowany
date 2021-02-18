'''Do klasy z poprzedniego zadania dodaj 3 metody:

show info, która

wyświetli wielkimi literami nazwę produktu

wyświetli informację o smaku

jeśli produkt ma jakieś dodatki to je wyświetli

jeśli produkt ma nadzienie to je wyświetli

(oczywiście przetestuj działanie funkcji po jej zaimplementowaniu)

set_filling, która

jako argument przyjmie nazwę nadzienia ciasta

zapisze ją w atrybucie filling dla ciasta

(oczywiście przetestuj działanie funkcji)

add_additives, która

jako argument przyjmie listę dodatków

wartości z listy doda do aktualnej listy dodatków

(tę funkcję też przetestuj)

Następnie dodaj do muffinki nadzienie kremowe, a do bezy dodaj kokos i posypkę kakaową. Tak zmodyfikowane wypieki wyświetl. Poniżej zobacz spodziewany efekt:

Today in our offer:
VANILLA CAKE
Kind:    cake
Taste:   vanilla
Additives:
	chocolade
	nuts
Filling: cream
--------------------
CHOCOLADE MUFFIN
Kind:    muffin
Taste:   chocolade
Additives:
	chocolade
Filling: vanilla cream
--------------------
SUPER SWEET MARINGUE
Kind:    meringue
Taste:   very sweet
Additives:
	cocoa powder
	coconuts
--------------------
'''

class Cake:
    def __init__(self,name,kind,taste,additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

    def ShowInfo(self):
        print("{}".format(self.name.upper()))
        print("Kind:    {}".format(self.kind))
        print("Taste:   {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
        print('-'*20)

    def set_filling(self, filling):
            self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


cake_01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake_02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake_03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

cake_01.ShowInfo()
cake_02.ShowInfo()
cake_03.ShowInfo()

cake_02.set_filling('vanilla cream')
cake_03.add_additives(['cocoa powder', 'coconuts'])


print("Today in our offer:")
for c in bakery_offer:
    c.ShowInfo()