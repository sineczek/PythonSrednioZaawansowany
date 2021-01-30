instruction = ['say hello', 'say how are You','abort','ask for money','say thank You','say bye']
instructionApproved = []

for instr in instruction:
    print('Adding instruction: ',instr)
    instructionApproved.append(instr)
    if instr == 'abort':
        print('Aborting!!!')
        instructionApproved.clear()
        break
else:
    print('Following action will be taken: ', instructionApproved)

print('\n-----------------------------\n')
instructionApproved.clear()
i = 0
while i < len(instruction):
    print('Adding instruction: ',instruction[i])
    instructionApproved.append(instruction[i])
    if instruction[i] == 'abort':
        print('Aborting!!!')
        instructionApproved.clear()
        break
    i+=1
else:
    print('Following action will be taken: ', instructionApproved)