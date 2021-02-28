import datetime as dt

class MilionDays:

    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year,month,day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()

md = MilionDays(200,1,1,2500000)

#print(md[0], md[1], md[10])

it = iter(md) #tworzenie iteratora aby next działał

print(next(it))
print(next(it))
print(next(it))


for d in md:
    pass

