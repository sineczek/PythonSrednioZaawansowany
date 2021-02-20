'''W tym zadaniu nadal pracujemy nad klasą "Ciastko"

Dodaj do klasy Cake ukryty atrybut gluten_free. (To jedna z ważniejszych informacji o wypiekach, dlatego staramy się,
żeby ten atrybut można było ustawić tylko raz podczas tworzenia obiektu, dzięki czemu później podczas pracy programu
nie zmienimy przypadkowo wartości w tym polu)

Zmień funkcję __init__ oraz show_info tak, aby obsługiwały nowy atrybut klasy

Tworząc nowe obiekty wypieków przekazuj wartość True lub False wskazującą na to czy wypiek jest bezglutenowy
(o ile wiem jajka nie zawierają glutenu, więc bezy są bezglutenowe)

Przetestuj działanie programu

Spróbuj w kodzie programu (np. po wyświetleniu oferty ciastkarni) zmienić atrybut __gluten_free

Czy po uruchomieniu masz błąd? Dlaczego? Korzystając z polecenia dir(cake03) zobacz jakie atrybuty ma ten obiekt

Zmień wartość atrybutu korzystając ze specjalnie i automatycznie utworzonego atrybutu o specyficznej budowie tak,
jak to było zrobione w materiale video

Wyświetl ponownie informacje o cake03 (beza) - czy teraz stała się wyrobem glutenowym?'''


class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []


    def __init__(self,name,kind,taste,additives, filling, glutenFree):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)
        self.__glutenFree = glutenFree

    def ShowInfo(self):
        print("{}".format(self.name.upper()))
        print("Kind:\t\t\t{}".format(self.kind))
        print("Taste:\t\t\t{}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:\t\t{}".format(self.filling))
        print("Gluten free:\t{}".format(self.__glutenFree))
        print('-'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


cake_01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', True)
cake_02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False)
cake_03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True)
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False)



print("Today in our offer:")
for c in Cake.bakery_offer:
    c.ShowInfo()