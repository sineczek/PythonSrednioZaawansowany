'''Zapisz poniższe polecenie if w postaci uproszczonej:

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)


'''
price = 123
bonus = 23
bonus_granted = True
price = price - bonus if bonus_granted else price
print(price)

'''Zapisz poniższe polecenie if w postaci uproszczonej:

rating = 5
 
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
'''
rating = 5
print('very good') if rating == 5 else print('good') if rating == 4 else print('week')



'''Ktoś był kiedyś niezadowolony, bo w kursie jest za mało polskich akcentów, więc... posłuchaj piosenki 
De Mono - Niedziela będzie dla nas - https://www.youtube.com/watch?v=lmn0Qf1_eI4 
(możesz też skorzystać z oryginalnej wersji: Niebiesko Czarnych: https://www.youtube.com/watch?v=Fxkhe8GqYkc)

Napisz program, który:

zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia

bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else ustali co dzisiaj powinieneś robić

Przepisz powyższy program stosując składnie uproszczona polecenia if'''

poniedzialek = 'pomagam mamie'
wtorek = 'masz w domu pranie'
sroda = wtorek
czwartek = 'dyżur'
piatek = 'dwa zebrania'
sobota = 'ty na lekcie ganiasz'
niedziela = 'będzie dla nas'

import datetime

today = datetime.datetime.today().weekday()
print(poniedzialek) if today == 0 else print(wtorek) if today == 1 else print(sroda) if today == 2 else print(czwartek) if today == 3 else print(piatek) if today == 4 else print(sobota) if today == 5 else print(niedziela)



