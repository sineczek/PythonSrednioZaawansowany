
isOk = 'True' #choć string to i tak if zadziałało to Python sam robi automatyczną konwersję
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = 'False' #a i tak wartość logiczna True
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = '' #teraz dopiero zinterpretuje jako False, czyli jak coś jest w napisie to zawsze jest prawdą czyli True
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = 1 # True, ujemne również, czyli znów jak coś jest to True
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')
isOk = 0 # False
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = [1,2,3] # przy liście to samo, jak coś jest to True, jak pusta to False
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = [0,0,0] #nadal True, chyba, że odwołamy się do 1 pozycji
print('Variable isOk: ', isOk, type(isOk))
if isOk[0]: #jak tak będzie to False, bo odwołujemy się do 0 czyli do pustego
    print('TRUE')

listOfErrors = [100,101,102]
print('Variable listOfErrors: ', listOfErrors, type(listOfErrors))
if listOfErrors: #zadziała bo były błedy, ale lepiej jak poniżej
    print('TRUE')

listOfErrors = [100,101,102]
print('Variable listOfErrors: ', listOfErrors, type(listOfErrors))
if len(listOfErrors) > 0:
    print('TRUE')




