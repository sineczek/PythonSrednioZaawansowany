import datetime

poczatek = datetime.date(2007,4,2)
koniec = datetime.date(2021,1,31)

iloscdni = koniec.weekday() - poczatek.weekday()

dnipracujace = ((koniec-poczatek).days - iloscdni) / 7 * 5 + min(iloscdni,5) - (max(koniec.weekday() - 4, 0) % 5)

print('Od podjęcia pracy w 02-04-2007 r, do końca stycznia 2021 minęło: ', dnipracujace, 'Od tego jeszcze trzeba odjąć dni świąteczne i wolne.')