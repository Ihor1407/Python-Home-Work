num = int(input('Введіть число: '))

while num > 9:
    num1 = 1

    for i in str(num):
        num1 = num1 * int(i)

    num = num1

print(num)
