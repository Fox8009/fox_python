# Осуществляется ввод данных списка с клавиатуры. Реализовать функцию, принимающую одно число и возвращающую его модуль.
# Вывести список абсолютных величин исходного списка. А также число -- количество вызовов функции.
# Не забыть обработать возможные исключения.

answer = []
counter = 0
try:
    l = list(map(float, (input('Enter the list: ')).split()))
    for i in l:
        answer.append(abs(i))
        counter += 1
    print(answer, 'The function has been called', counter, 'times')
except ValueError:
    print('Not a number')
except Exception:
    print('Impossible to fulfill')
else:
    print('Completed without errors')

# Вводятся с клавиатуры 2 списка.
# Реализовать поэлементное умножение элементов первого списка на элементы второго.

answer = []
try:
    l1 = list(map(float, (input('Enter the list1: ').split())))
    l2 = list(map(float, (input('Enter the list2: ').split())))
    for i in range(max(len(l1), len(l2))):
        answer.append(l1[i]*l2[i])
    print(answer)
except IndexError:
    print('List index out of range')
except ValueError:
    print('Not a number entered')


# Дана строка с пробелами (с несколькими словами). Вывести длину слов в строке, используя функцию map().
string = input('Enter:')
string = string.split()
print(list(map(len, string)))
