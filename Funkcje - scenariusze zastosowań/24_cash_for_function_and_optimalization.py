import time
import functools

#bez optymalizacji
def Factorial(n):

    time.sleep(0.1) #opóźnienie o 0.1 sekundy !!
    if n == 1:
        return 1
    else:
        return n*Factorial(n-1)

start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Czas wykonania bez optymalizacji: ', stop-start)

#z "optymilizacja"
@functools.lru_cache()
def Factorial(n):

    time.sleep(0.1) #opóźnienie o 0.1 sekundy !!
    if n == 1:
        return 1
    else:
        return n*Factorial(n-1)

start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Czas wykonania z optymalizacją: ', stop-start)

print(Factorial.cache_info()) #CacheInfo(hits=9, misses=10, maxsize=128, currsize=10)
# hits to ile razy trafiliśmy wynik | misses ile razy nie było wyniku w cachu |
# max to ile maksymalnie można | curr to ile jest obecnie








#gdy raz jeszcze się wykona, to od razu wszystko jest w cashu i wynik jest natychmiastowy
'''start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Czas wykonania z optymalizacją: ', stop-start)'''