# numbers = [12, 3, 4, 10]
# numbers = [1]
# numbers = []
numbers = [12, 3, 4, 10, 8]

if len(numbers) > 1:
    poped_numbers = numbers.pop()
    numbers.insert(0, poped_numbers)

print(numbers)
