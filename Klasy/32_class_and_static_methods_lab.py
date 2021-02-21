'''Dlaczego warto wykonywać zadania? Bo w tym zadaniu będzie ciekawie. Skorzystasz z 2 fantastycznych funkcji, których
nie omówiłem na kursie. Ale po kolei:

Naszym zadaniem jest zapisanie na dysku informacji o wyrobach naszej cukierni. Obiekty klasy Cake są już trochę
skomplikowane, wiec do ich eksportowania na dysk i importowania z dysku wykorzystamy moduł pickle.
(Kilka słów o module i link do dokumentacji znajdziesz poniżej), a tu krótkie streszczenie:

Moduł zaimportujesz komendą

import pickle

Jeśli f to uchwyt do pliku, a obj to jakiś obiekt, to możesz go zapisać na dysku poleceniem:

pickle.dump(obj, f)

A jeśli potem ten obiekt chcesz odczytać, to możesz to zrobić tak:

new_obj = pickle.load(f)



No to do roboty.

Dodaj do klasy funkcję save_to_file. Funkcja ma pracować na poziomie instancji

Funkcja ma przyjąć argument path wskazujący na ścieżkę dostępu do pliku

Plik należy otworzyć do zapisu w trybie binarnym i korzystając z pikle.dump zapisać bieżący obiekt do pliku

Przetestuj działanie funkcji zapisując cake01 i cake02 do plików. Nadaj plikom rozszerzenie bakery



Dodaj do klasy funkcję read_from_file. Funkcja ma przyjmować jako argument ścieżkę do pliku

Funkcja ma otworzyć plik na odczyt w trybie binarnym i wczytać obiekt klasy Cake z tego pliku korzystając z pickle.load

Nowy obiekt należy dopisać do zmiennej klasy bakery_offer i zwrócić ten obiekt

Przetestuj działanie funkcji wczytując plik z poprzedniego przykłądu do nowego obiektu np. cake05. Aby przetestować
czy wszystko się udało wywołaj dla tego nowego obiektu z funkcji show_info



No dobrze, ale jeśli znamy ścieżkę dostępu do katalogu i  w tym katalogu znajdują się pliki z rozszerzeniem bakery,
to chcielibyśmy mieć funkcję , która zwróci listę takich plików. Odpowiednią do tego prawie gotową funkcję znajdziesz
w module glob:

import glob

Aby otrzymać listę plików z rozszerzeniem txt z katalogu c:/temp możesz wywołać funkcję:

glob.glob('c:/temp/*.txt')



Dodaj do klasy Cake funkcję statyczną get_bakery_files, która jako argument przyjmie nazwę katalogu

Funkcja ma zwrócić listę plików z rozszerzeniem bakery z przekazanego argumentem katalogu

Przetestuj działanie funkcji

'''

import pickle
import glob

class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free,text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return __text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')

    def save_to_file(self, path):
        with open(path,'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path,'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog+'/*.bakery')

cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Good luck!')

cake01.save_to_file(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Klasy\lab_files\cake01.bakery')
cake02.save_to_file(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Klasy\lab_files\cake02.bakery')

cake05 = Cake.read_from_file(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Klasy\lab_files\cake01.bakery')
cake05.show_info()

print(Cake.get_bakery_files(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Klasy\lab_files'))