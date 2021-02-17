'''Szef cukierni w której pracujesz poprosił Cię o napisanie programu, który koniecznie ma działać obiektowo!

Zaczynamy od zdefiniowania klasy Cake, która ma posiadać atrybuty:

-name opisujące nazwę produktu

-kind opisujący rodzaj wypieku np. torty, ciastka, muffinki, bezy

-taste z głównym smakiem

-addictions - zawierający listę dodatków do danego ciasta, np. owoce, posypki, polewy itp, jeżeli ciasto nie ma dodatków,
to będzie to pusta lista

-filling - opis nadzienia, jeżeli dane ciasto nie ma nadzienia, to ma to być pusty napis

-... możesz dodać dalsze własne pomysły :)



Po zdefiniowaniu klasy utwórz kilka instancji tej klasy, to dobry moment na wzbogacenie słownictwa w zakresie słodkości
w języku angielskim, ale jak wolisz - możesz to robić po polsku



Utwórz listę bakery_offer i dodaj do niej instancje wcześniej utworzonych obiektów klasy Cake



Napisz pętlę przechodzącą przez wszystkie instance klasy znajdujące się na liście bakery_offer i wyświetl coś w rodzaju
(dane pochodzące z instancji zostały wytłuszczone):

Today in our offer:

Vanilla Cake - (cake) main taste: vanilla with additives of ['chocolade', 'nuts'], filled with cream

Chocolade Muffin - (muffin) main taste: chocolade with additives of ['chocolade'], filled with

Super Sweet Maringue - (meringue) main taste: very sweet with additives of [], filled with



UWAGA: w kolejnych lekcjach i kolejnych zadaniach będę kontynuował temat cukierni. W większości przypadków zadanie
będzie polegało na rozbudowaniu tej klasy. Jeżeli chcesz wykonać wiecej zadań pozwalających Ci lepiej opanować tematykę klas,
podrzucam kilka pomysłów poniżej. Do tych pomysłów nie publikuję propozycji rozwiązań. Za to możesz takie własne rozwiązania
i propozycje publikować w sekcji Q&A . Możesz też próbować budowania klas z takimi tematami jak sam zechcesz.

"Sklep z używanymi telefonami komórkowymi"

"Warsztat wulkanizacyjny"

"Inwentaryzacja sprzętu komputerowego w firmie"

"Studio fitness"

"Karty gwarancyjne"

"Firma przewozowa - taxi bagażowe"

"Biuro podróży"

...'''

class Cake:
    def __init__(self,name,kind,taste,additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

cake_01 = Cake('Vanila Cake','cake','vanilla',['chcolade', 'nuts'],'cream')
cake_02 = Cake('Chocolade Muffin','muffin','chocolade',['chocolade'],'')
cake_03 = Cake('Super Sweet Maringue','meringue','very sweet',[''],'')

'''print(cake_01.name,cake_01.kind,cake_01.taste,cake_01.additives,cake_01.filling)
print(cake_02.name,cake_02.kind,cake_02.taste,cake_02.additives,cake_02.filling)
print(cake_03.name,cake_03.kind,cake_03.taste,cake_03.additives,cake_03.filling)
'''
bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

print("Today in our offer:")
for c in bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(
        c.name, c.kind, c.taste, c.additives, c.filling))




