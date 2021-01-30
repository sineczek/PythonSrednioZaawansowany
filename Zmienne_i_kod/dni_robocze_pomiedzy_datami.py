import datetime
import os
print('Policzmy ile dni pracujesz !!!')
print('Daty wprowadzaj w formacie yyyy-mm-dd')
date1 = input('Podaj kiedy rozpocząłeś pracę: ')
date2 = input('Podaj kiedy do kiedy obliczyć: ')
byear, bmonth, bday = map(int, date1.split('-'))
eyear, emonth, eday = map(int, date2.split('-'))
begining = datetime.date(byear, bmonth, bday)
end = datetime.date(eyear, emonth, eday)

days = (end-begining).days
years = end.year - begining.year
weekdays = end.weekday() - begining.weekday()
weeks = ((end-begining).days - weekdays) / 7

workdays = ((end-begining).days - weekdays) / 7 * 5 + min(weekdays,5) - (max(end.weekday() - 4, 0) % 5)
leave = float(weeks / (26/12))
holidays = 13#input('Podaj ile średnio przypada dni ustawowo wolnych, w Polsce jest to 13: ')
nWD= float(holidays)*years
#print('workdays :', type(workdays), workdays, '\nleave: ', type(leave),leave, '\nnotWorkingDays: ', type(notWorkingDays),notWorkingDays, '\nnWD: ', type(nWD),nWD)
print('Maksymalna ilość dni urpopowych, która Ci przysługiwała w tym okresie to: ', round(leave))
leaveused = input('Czy wszystkie dni urlopowe wykorzystałeś? T/N: ')
if leaveused.upper() == 'N':
    usedleave = input('Ile dni wykorzystałeś?')
else:
    usedleave = leave
usedleave = float(usedleave)

print('Od podjęcia pracy w ', begining,'r., do ', end, 'minęło: ', days, 'w tym ', workdays, 'dni pracujących.')
print('Srednio w roku jest 13 dni ustawowo wolnych, co pozostawia: ', workdays-(14*13),'przepracowanych dni')
print('Od tego jeszcze odjąć ilość dni wykorzystanego urlopu ', round(usedleave))
print('Sumując, od podjęcia pracy do wskazanego dnia przepracowałeś ', workdays-nWD-usedleave)
print('Czyli nie pracowałeś przez: ', days-workdays,'w tym ustawowo wolnych było: ', nWD)
print('W powyższych obliczeniach nie uwzględniono dni spędzonych na chorobowym!')