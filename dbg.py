# l1 = [1, 3, 2, 5, 7, 4]
# l2 = [0, 4, 6, 3, 7, 4]
# l3 = []
# for i, j in zip(l1, l2):
#     if i > j:
#         l3.append(i)
# print(l3)

# l1 = [1, 3, 2, 5, 7, 4]
# l2 = [0, 4, 6, 3, 7, 4]
# l3 = []
# for i, j in zip(l1, l2):
#     l3.append(i if i > j else j)
# print(l3)

# names = ["Sam", "John", "Lindsay", "Anna"]
# last_names = ["Smith", "Black", "Johnson", "Davis"]
# full_names = []
# for i, j in zip(names, last_names):
#     full_names.append("{} {}".format(i, j))
# print(full_names)



# except ValueError:
#     print('Not an integer entered')
# except Exception:
#     print('Impossible to fulfill')

# Вводятся с клавиатуры 2 списка.
# Реализовать поэлементное умножение элементов первого списка на элементы второго.

# answer = []
# try:
#     l1 = list(map(int, (input('Enter the list1: ').split())))
#     l2 = list(map(int, (input('Enter the list2: ').split())))
#     for i in range(max(len(l1), len(l2))):
#         answer.append(l1[i]*l2[i])
#     print(answer)
# except IndexError:
#     print('List index out of range')
# except ValueError:
#     print('Not a number entered')


# Дана строка с пробелами (с несколькими словами). Вывести длину слов в строке, используя функцию map().
# string = input('Enter:')
# string = string.split()
# print(list(map(len, string)))

l1 = []
c = 0
l = list((map(int, input().split())))
for i in range(len(l)):
  l1.append(abs(l[i]))
  c += 1
print(l1)

