a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a<b:
    for i in range(a, b+1):
        print(i)
else:
    for x in range(a, b-1, -1):
        print(x)
