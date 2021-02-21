'''W tym LAB pracujemy z klasą z poprzedniej lekcji (jeśli nie masz rozwiązania skopiuj sobie moją propozycję rozwiązania
z poprzedniej lekcji)

Do klasy należy dodać atrybut ukryty __text. Odpowiada on za napis umieszczony na torcie.

W funkcji __init__ przyjmij nowy argument text

Zapisz go w zmiennej __text przeprowadzając kontrolę: napis można zapisać w instancji tylko jeżeli kind jest 'cake' lub
text jest napisem pustym. Jeśli te warunki nie są spełnione wyświetl diagnostyczny komunikat (print dla Ciebie, żeby
było wiadomo co się dzieje)

Dodaj ukrytą funkcję __get_text, która będzie zwracać wartość zapisaną w __text

Dodaj ukrytą funkcje __set_text, która przyjmie dodatkowy argument new_text i zaktualizuje atrybut __text tylko dla
wyrobów z kind 'cake'

Zdefiniuj właściwość Text korzystającą z powyższych funkcji.

Tworząc obiekty klasy Cake przekaż dodatkowy argument text - umieść napisy puste lub inne typowo  "tortowe", część
poprawnych (czyli napis na torcie) i część niepoprawnych (np. napis na waflu)

Wyświetl wszystkie informacje o wszystkich wypiekach

Spróbuj wstawić do właściwości Text napis na torcie i na innym wypieku nietortowym - prześledź poprawność tych operacji
ponownie wyświetlając ofertę cukierni'''


class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []


    def __init__(self,name,kind,taste,additives, filling, glutenFree, text):
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
        if kind == 'cake' or text =='':
            self.__text = text
        else:
            self.__text = ''
            print('>>Text can be set only for cake({})<<'.format(name))


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
        if len(self.__text) > 0:
            print('Text:\t\t\t{}'.format(self.__text))

        print('-'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>Text can be set only for cake({})<<'.format(self.name))


cake_01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake_02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
cake_03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True, '')
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Good luck!')


print("Today in our offer:")
for c in Cake.bakery_offer:
    c.ShowInfo()

cake_01.Text = 'Happy birthday!'
cake_02.Text = '18'

for c in Cake.bakery_offer:
    c.ShowInfo()