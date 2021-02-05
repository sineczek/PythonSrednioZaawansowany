import time

source = 'reportLine += 1'

reportLine = 0
start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
timeNotCompiled = stop - start

start = time.time()
#uruchamianie kodu scompilowanego jest o wiele szybsze
sourceCompiled = compile(source,'Internal variable source', 'exec')
#compile(co? - tu np. odnośnik do pliku - gdzie ma być przekaan exec, eval, simple,

for i in range(100000):
    exec(sourceCompiled)
stop = time.time()
timeCompiled = stop - start

print(reportLine)
print('Time not compiled: ', timeCompiled)
print('TIme compiled: ', timeCompiled)
print('How much faster? ', timeNotCompiled/timeCompiled)






