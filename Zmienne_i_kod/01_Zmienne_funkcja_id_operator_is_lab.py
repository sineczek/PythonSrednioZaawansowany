'''W tym zadaniu sprawdzimy, jak zachowują się zmienne podczas modyfikowania ich wartości

W pierwszym przypadku zainicjuj zmienne a, b, c wartością 10. W tym celu wykonaj tylko

jedną instrukcję.

Wyświetl wartości zmiennych oraz ich identyfikatory

Następnie zmień wartość zmiennej a np. na 20

Ponownie wyświetl wartości zmiennych i ich identyfikatory

(identyfikator zmiennej a powinien się zmienić)

'-----------------------------

Teraz wykonaj jeszcze raz te same czynności, co poprzednio ale z delikatną różnicą:

zmienne a, b i c mają mieć przypisaną wartość w postaci listy, np. [1,2,3]

modyfikacja zmiennej a ma polegać na dodaniu do listy a nowego elementu, np. liczby 4

(identyfikator zmiennej a powinien być teraz taki sam jak b i c, dodatkowo zmieni się jednocześnie lista w zmiennych b i c)

-----------------------------

Dlaczego tak się stało? - poniżej próbuję to wyjaśnić, ale prawdziwe wyjaśnienie zobaczysz w kolejnej lekcji:

W pierwszym przykładzie a, b, c były wskaźnikami do komórki pamięci, w której była zapisana liczba, czyli końcowa wartość.

W drugim przykładzie a, b, c to wskaźnik do komórki pamięci, w której jest lista. Lista jest wskaźnikiem do elementów tej listy.
Kiedy dodajesz nowy element do listy, nie modyfikujesz podstawowej komórki pamięci z listą, dlatego id się nie zmienił.

-----------------------------

Uwaga - w tym zadaniu można się spodziewać, że w różnych wersjach Pytona uzyskamy różne wyniki, ale spróbujmy...

Do zmiennej x przypisz wartość 10

Do zmiennej y przypisz wartość 10 (użyj przypisań w dwóch osobnych liniach!)

Wyświetl id tych zmiennych

(chociaż mamy do czynienia z dwoma niezależnymi zmiennymi, to optymalizator pythona nadał im ten sam id)

-----------------------------

Do zmiennej y przypisz wartość y plus 1 minus 1.

Sprawdź identyfikatory zmiennych x i y

(identyfikatory nadal powinny być takie same, tzn. optymalizator poradził sobie z prostym działaniem + 1 - 1)

-----------------------------

Powtórz operację dodawania i odejmowania od y, ale tym razem dodaj i odejmij wartość 1234567890

Sprawdź identyfikatory zmiennych x i y

(identyfikatory powinny być różne, tzn. optymalizator nie rozpoznał, że zmienne mają nadal te same wartości)'''

a = b = c = 10
print('Zmienna "a"', a,'ID zmiennej "a"', id(a),'\nZmienna "b"', b,'ID zmiennej "b"', id(b),'\nZmienna "c"', c,'ID zmiennej "c"', id(c))
a = 20
print('\nZmienna "a"', a,'ID zmiennej "a"', id(a),'\nZmienna "b"', b,'ID zmiennej "b"', id(b),'\nZmienna "c"', c,'ID zmiennej "c"', id(c))

a = b = c = [1,2,3]
print('\nZmienna "a"', a,'ID zmiennej "a"', id(a),'\nZmienna "b"', b,'ID zmiennej "b"', id(b),'\nZmienna "c"', c,'ID zmiennej "c"', id(c))
a.append(4)
print('\nZmienna "a"', a,'ID zmiennej "a"', id(a),'\nZmienna "b"', b,'ID zmiennej "b"', id(b),'\nZmienna "c"', c,'ID zmiennej "c"', id(c))

x = 10
y = 10
print('\nZmienna "x"', x,'ID zmiennej "x"', id(x),'\nZmienna "y"', y,'ID zmiennej "y"', id(y))
y = y+1-1
print('\nZmienna "x"', x,'ID zmiennej "x"', id(x),'\nZmienna "y"', y,'ID zmiennej "y"', id(y))
y = y+1234567890-1234567890
print('\nZmienna "x"', x,'ID zmiennej "x"', id(x),'\nZmienna "y"', y,'ID zmiennej "y"', id(y))
