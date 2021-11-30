# Дан список a = [5, 7, -3, -7, 65, 34, 23, -12, -9].
# Отсортировать таким образом, чтобы сначала шли отрицательные, потом положительные в порядке возрастания абсолютного
# значения (модуля) числа. (т.е. -3, -7, -9, -12, 5, 7, 23, 34, 65)

a = [5, 7, -3, -7, 65, 34, 23, -12, -9]
minus = []
plus = []
for i in a:
    if i < 0:
        minus.append(abs(i))
    else:
        plus.append(i)
print([i * -1 for i in sorted(minus)] + sorted(plus))

# Реализовать Insertion Sort (Сортировка вставками)
listToSort = [5, 7, -3, -7, 65, 34, 23, -12, -9]
for i in range(1, len(listToSort)):
    current = listToSort[i]
    j = i - 1
    while j >= 0 and listToSort[j] > current:
        listToSort[j + 1] = listToSort[j]
        j -= 1
    listToSort[j + 1] = current

print(listToSort)
