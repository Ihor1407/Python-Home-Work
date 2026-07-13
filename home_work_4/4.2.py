num = []

num1 = num[::2]

new_sum = sum(num1) * num[-1] if num else 0
print(new_sum)
