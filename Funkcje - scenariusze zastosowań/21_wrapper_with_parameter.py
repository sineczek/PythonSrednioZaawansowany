import datetime
import functools

''' PRZED URUCHOMIENIEM TRZEBA WYCIĄ TO CO W KOMENTARZU
logFilePath = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Funkcje - scenariusze zastosowań\lab_files\log.txt'

def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        file = open(logFilePath, "a")
        file.write('-'*20 + '\n')
        file.write('Function "{}" started at {}\n'.format(func.__name__, datetime.datetime.now().isoformat()))
        file.write('Following arguments ware used:\n')
        file.write(' '.join('{}'.format(x) for x in args))
        file.write('\n')
        file.write(' '.join('{}={}'.format(k,v) for (k,v) in kwargs.items()))
        file.write('\n')
        result = func(*args, **kwargs)
        file.write('function returned {}\n'.format(result))
        file.close()
        return result
    return func_with_wrapper
'''

def CreateFunctionWithWrapper_LogToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, "a")
            file.write('-'*20 + '\n')
            file.write('Function "{}" started at {}\n'.format(func.__name__, datetime.datetime.now().isoformat()))
            file.write('Following arguments ware used:\n')
            file.write(' '.join('{}'.format(x) for x in args))
            file.write('\n')
            file.write(' '.join('{}={}'.format(k,v) for (k,v) in kwargs.items()))
            file.write('\n')
            result = func(*args, **kwargs)
            file.write('function returned {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper

@CreateFunctionWithWrapper_LogToFile(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Funkcje - scenariusze zastosowań\lab_files\change_salary_log.txt')
def ChangeSalary(employ_name, new_salary, is_bonus = False):
    print('Changing salary for {} to {} as bonus = {}'.format(employ_name,new_salary,is_bonus))
    return new_salary

@CreateFunctionWithWrapper_LogToFile(r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\SrednioZaawansowany\Funkcje - scenariusze zastosowań\lab_files\change_position_log.txt')
def ChangePosition(employ_name, new_position):
    print('Changing posiotion {} to {} '.format(employ_name,new_position))
    return new_position


print(ChangeSalary('Johnson',20000,True))
print(ChangeSalary('Johnson',20000,is_bonus=True))
print(ChangePosition('Michael','Salesman'))
print(ChangePosition('Margaret','Manager'))