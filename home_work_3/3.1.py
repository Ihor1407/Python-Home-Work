num1 = float(input('Введіть перше число: '))
operator = input("Введіть дію (+,-,/,*):")
num2 = float(input("Введіть друге число: "))


if operator == '+':
    print(f"відповідь: {num1 + num2}")
elif operator == '-':
    print(f"Відповідь: {num1 - num2}")
elif operator == '/':
    if num2 == 0:
        print("Дiлення на 0 заборонено")
    else:
        print(f"Відповідь: {num1 / num2}")
elif operator == '*':
    print(f"Відповідь: {num1 * num2}")