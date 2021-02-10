#wrapper - funkcja śledzi inne funkcje
import datetime
import functools

def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('Function "{}" started at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
        print('Following arguments ware used:')
        print(args, kwargs) #ten słownik jest pusty {} chyba  że - print no 2
        result = func(*args, **kwargs)
        print('function returned {}'.format(result))
        return result
    return func_with_wrapper

@CreateFunctionWithWrapper #dekorowanie funkcji
def ChangeSalary(employ_name, new_salary, is_bonus = False):
    print('Changing salary for {} to {} as bonus = {}'.format(employ_name,new_salary,is_bonus))
    return new_salary

#print(ChangeSalary('Johnson', 20000, True))



#ChangeSalary = CreateFunctionWithWrapper(ChangeSalary) #to jest obudowywanie funkcji ale lepiej to zrobić @CreateFunctionWithWrapper
#1
print(ChangeSalary('Johnson',20000,True))

#2
print(ChangeSalary('Johnson',20000,is_bonus=True))




