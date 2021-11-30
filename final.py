# Считать с клавиатуры 2 числа. Вывести наименьшее из них по модулю.

# num1 = abs(float(input()))
# num2 = abs(float(input()))
# print(num1 if num1 < num2 else num2)

# Считать с клавиатуры строку. Вывести количество слов в данной строке. (напр., “Мама мыла раму” -- 3 слова. “helloworld” -- 1 слово)

# def count_words(string):
#     return len(string.split())
#
# string = input()
# print(count_words(string))

# Дан список array = [10,9,3,7,5,1,3,2]. Отсортировать его по убыванию методом пузырька.

# array = list(map(int, input().split())) - это если вводить список с клавиатуры
# array = [10, 9, 3, 7, 5, 1, 3, 2]
# for k in range(len(array)-1):
#     for i in range(len(array) - 1):
#         if array[i] < array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
# print(array)

# Квадратная матрица имеет следующий вид:
# 1  2  3  4  …
# 2  2  3  4  …
# 3  3  3  4  …
# 4  4  4  4  …
# …………….
# Считать число с клавиатуры, сформировать и вывести такую матрицу, имеющую введенное количество строк и столбцов
# m = int(input())
# matrix = []
# for i in range(m):
#     matrix.append(m*[0])
#
# for row in range(m):
#     for col in range(m):
#         matrix[row][col] = col + 1 if col >= row else row + 1
#
# for row in matrix:
#     print(*row)






# Реализовать функцию, возвращающую значение f(x) = 5*sin(x).
# Считать с клавиатуры 2 числа, являющиеся началом и концом некоторого интервала. Вычислить значение интеграла функции f(x) на этом интервале с помощью метода трапеций.

# from math import sin
#
#
# def f(x):
#     return 5 * sin(x)
#
#
# x1 = float(input())
# x2 = float(input())
# integral = 0
# s = 0.5 * (f(x1) + f(x2))
# h = (x2 - x1) / 1000
# x = x1 + h
# while x <= x2 - h:
#     s += f(x)
#     x += h
# integral = h * s
# print("По методу трапеций: ", integral)


# В таблице Excel https://docs.google.com/spreadsheets/d/1OKhkSS66cSfVBcBHc9K3gTmWNvW_R5Y2/edit?usp=sharing&ouid=102065312584855924846&rtpof=true&sd=true
# находятся данные по ценам акций компаний ConocoPhillips и EOG Resources в период с 03.01.2011 по 31.01.2014
# Отобразить динамику цен обеих компаний на одном графике.
# Оценить коэффициенты регрессии вектора цен одного актива на другой
# Представить другой актив линейной комбинацией от первого
# Построить график
# Добавить линию среднего
# Добавить верхний и нижний “коридоры”, отклоняющиеся от среднего на величину стандартного отклонения
