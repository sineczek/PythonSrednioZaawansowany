# tak raczej nie należy
# file = open(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\data.txt')
#
# data = file.read()
#
# file.close()
#
# for line in data.splitlines():
#    if line.startswith('ACTION'):
#        print(line)


# tak lepiej
# file = open(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\data.txt')
#
# for line in file:
#    if line.startswith('ACTION'):
#        print(line.replace('\n', ''))
#
# file.close()

# coś jak translator robiący tuple
#file = open(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\data.txt')
#
#records = []
#
#for line in file:
#   if ':' in line:
#       type, action = line.rstrip("\n").split(':', 1)
#       record = (type, action)
#        records.append(records)
#
#print(records)
#
#file.close()


def get_records(filepath):
    print('----- opening file -----')
    file = open(filepath)

    for line in file:
        if ':' in line:
            type, action = line.rstrip("\n").split(':', 1)
            record = (type, action)
            yield record

    print('----- closing file -----')
    file.close()

for record in get_records(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Generatory\lab_files\data.txt'):
    print('The type is {} and the action is {}'.format(record[0], record[1]))




