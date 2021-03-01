import datetime as dt


def MilionDays(year, month, day, maxdays):
    date = dt.date(year, month, day)

    for i in range(maxdays):
        yield (date + dt.timedelta(days=i))  # generator zwraca wartośc i zamraża funkcję do kolejnego wywołania


for d in MilionDays(2000, 1, 1, 3):
    print(d)
print('-'*20)

def GetMagicNumbers():
    yield (22)
    yield (4)
    yield (5)

r = GetMagicNumbers()
#print(next(r))
#print(next(r))
#print(next(r))

#for aby nie było exception StopIteration
for m in r:
    print(m)

