import random

num = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
print(f'Звичайний список: {num}')

new_num = [num[0], num[2], num[-2]]
print(f'Новий список: {new_num}')
