# try:
#    with open(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Context Manger\lab_files\my_bad*_file.txt', 'w+') as file:
#        file.writelines('SUCCESS')
# except OSError as e:
#    print('Error opening file: {}\nDetails: {}'.format(e.filename, e.strerror))
#

import time


class time_messure:

    def __init__(self):
        pass

    def __enter__(self):
        print('entering ...')
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting ...')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print('Execution time: {}'.format(self.__difference))

with time_messure() as my_timer:
    time.sleep(3)




