'''Zmień go stosując następujące techniki:

zmień definicję zmiennych na słownik z właściwościami

zmień definicję funkcji, tak aby przyjmowała jeden parametr i nadal wyświetlała informacje przekazane parametrem

utwórz listę tortów i przechodząc przez nią wyświetl informacje zwracane przez funkcje show_cake_info'''

cake_01_taste = 'vanilia'
cake_01_glaze = 'chocolade'
cake_01_text = 'Happy Brithday'
cake_01_weight = 0.7

cake_02_taste = 'tee'
cake_02_glaze = 'lemon'
cake_02_text = 'Happy Python Coding'
cake_02_weight = 1.3


def show_cake_info(taste, glaze, text, weight):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        taste, glaze, text, weight))

show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)

print ('='*30)
cake_01 = {'taste'  : 'vanilia',
           'glaze'  : 'chocolade',
           'text'   : 'Happy Brithday',
           'weight' : 0.7 }


cake_02 = {'taste'  : 'tee',
           'glaze'  : 'lemon',
           'text'   : 'Happy Python Coding',
           'weight' : 1.3 }

def show_cake_info(a_cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        a_cake['taste'], a_cake['glaze'], a_cake['text'], a_cake['weight']))

cakes = [cake_01, cake_02]

for a_cake in cakes:
    show_cake_info(a_cake)







