dayType = 3

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass #nic nie robi, jest placeholderem w tej postaci
elif dayType == 2:
    pass
else:
    pass

#składnia uproszczona - jeśli coś trzeba tylko podmienić
dayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
print(dayDescription)

print('weekend') if dayType == 1 else print('workday') if dayType == 2 else print('holiday')




