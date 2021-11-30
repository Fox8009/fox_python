# первая задача

a = int(input('Enter the number: '))
if 10 <= a <= 99:
    print((a // 10) + (a % 10) * 10)
elif 100 <= a <= 999:
    b = a // 100
    c = (a // 10) % 10
    d = a % 10
    print(d * 100 + c * 10 + b)
else:
    print('Error')


# вторая задача
min = int(input('Enter the number: '))
if 0 <= min <= 15:
  print('First quarter of an hour')
elif 16 <= min <= 30:
  print('Second quarter of an hour')
elif 31 <= min <= 45:
   print('Third quarter of an hour')
elif 46 <= min <= 59:
   print('Fourth quarter of an hour')
else:
    print('Error')
