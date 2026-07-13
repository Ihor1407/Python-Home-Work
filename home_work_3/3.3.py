# numbers = [1, 2, 3]
# numbers = [1]
# numbers = []
numbers = [1, 2, 3, 4, 5, 6]
# numbers = [1, 2, 3, 4, 5]

midle = (len(numbers) + 1) // 2
separated = [numbers[:midle], numbers[midle:]]

print(separated)
