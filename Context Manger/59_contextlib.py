class Door:

    def __init__(self, where):
        self.where = where

    def open(self):
        print('Opening the door to the {}'.format(self.where))

    def close(self):
        print('Closing the door to the {}'.format(self.where))


# context manager bez __enter__ i __exit__

# door1 = Door('hell')
# door2 = Door('future')

# door1.open()
# door1.close()
# door2.open()
# door2.close()

#from contextlib import contextmanager
#
#@contextmanager
#def OnlyClose(obj):
#    yield obj
#    obj.close()
#
#with OnlyClose(Door('next room')) as door:
#    door.open()
#    print('The door is to the {}'.format(door.where))

#from urllib.request import urlopen
#from contextlib import closing

#with closing(urlopen('http://www.kursyonline24.eu')) as page:
#    for line in page:
#        print(line)

#import os
#os.remove(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Context Manger\lab_files\jakis_plik.txt')

#from contextlib import suppress
##with suppress(FileNotFoundError):           #ukrywanie wyjątku
#    os.remove(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Context Manger\lab_files\jakis_plik.txt')
    
from contextlib import redirect_stdout
f = open(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Context Manger\lab_files\jakis_plik.txt', 'w')
with redirect_stdout(f):
    print('Hello')
    d = Door('EXIT')
    d.open()
    d.close()