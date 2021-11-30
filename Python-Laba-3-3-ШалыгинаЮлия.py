# Даны 2 списка, содержащие одинаковое количество числовых элементов.
# l1 = [1,3,2,5,7,4]
# l2 = [0,4,6,3,7,4]
# Вывести элементы первого списка, которые больше элементов второго, стоящие на одинаковых позициях (сравнивать первый с первым, второй со вторым и тд)

l1 = [1, 3, 2, 5, 7, 4]
l2 = [0, 4, 6, 3, 7, 4]
l3 = []
for i in range(len(l1)):
       if l1[i] > l2[i]:
           l3.append(l1[i])
print(l3)


# Даны 2 списка, содержащие одинаковое количество числовых элементов.
# l1 = [1,3,2,5,7,4]
# l2 = [0,4,6,3,7,4]
# Для каждой позиции вывести наибольший элемент из соответствующего списка.

l1 = [1, 3, 2, 5, 7, 4]
l2 = [0, 4, 6, 3, 7, 4]
l3 = []
for i in range(len(l1)):
    if l1[i] >= l2[i]:
        l3.append(l1[i])
    else:
        l3.append(l2[i])
print(l3)



# names = [‘Sam’, ‘John’, ‘Lindsay’, ‘Anna’]
# last_names = [‘Smith’, ‘Black’, ‘Johnson’,’Davis’]
# В первом списке хранятся имена людей. Во втором хранятся их фамилии. Напечатать список данных людей в формате:
# Имя_1 Фамилия_1
# Имя_2 Фамилия_2

names = ["Sam", "John", "Lindsay", "Anna"]
last_names = ["Smith", "Black", "Johnson", "Davis"]
full_names = []
for i in range(len(names)):
       full_names.append(names[i] + " " + last_names[i])
print(full_names)
