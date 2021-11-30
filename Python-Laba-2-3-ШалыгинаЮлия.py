# С клавиатуры считывается число n. Требуется вывести последовательность “010101010...”, в которой ровно n символов. (Не n пар “01”, а именно n символов)
#
n = int(input("Enter the number: "))
for i in range(n):
    print(i % 2, end="")




# # Посчитать факториал числа с помощью цикла (факториал -- это произведение всех натуральных чисел от 1 до данного включительно, напр. 5! = 1*2*3*4*5 = 120)
number = int(input("Enter the number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("Factorial of a number", number, "is", factorial)


# Посчитать сумму всех делителей числа ( число 12 имеет делители 1, 2, 3, 4, 6, 12. Их сумма = 1+2+3+4+6+12 = 28)

n = int(input("Enter the number: "))
s = 0
for i in range(1, n+1):
    if n % i == 0:
        s += i
print("The sum of divisors of a number", n, "is", s)






