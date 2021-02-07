#zmienna wskazująca na funkcję

def BuyMe(what):
    print('Buy me', what)

BuyMe('a new car')
StealForMe = BuyMe
print(type(StealForMe)) #funkcja
StealForMe('a new car')


#automatyczna restauracja - dowóz robotem do stolika
def GoLeft(*args):
    print('PLACEHOLDER - turning left with', *args)

def GoRight(*args):
    print('PLACEHOLDER - turning right with', *args)

def GoForward(*args):
    print('PLACEHOLDER - going forward with', *args)

def GoBack(*args):
    print('PLACEHOLDER - going back with', *args)

def Start(*args):
    print('PLACEHOLDER - starting with', *args)

def Stop(*args):
    print('PLACEHOLDER - stopping with', *args)

#dojazd do stolika 1 - lista funkcji
instructions = [Start, GoForward, GoForward, GoLeft, GoForward, GoRight, Stop]

dish = 'pizza'
for instr in instructions:
    instr(dish)







