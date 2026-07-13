import string

my_input = input(f'Введіть дві літери через дефіс("b-e"):')
start_letter, end_letter = my_input.split('-')

letters = string.ascii_letters
sec_letters = letters.index(start_letter)
end_letters = letters.index(end_letter)

new_letters = letters[sec_letters:end_letters + 1]

print(new_letters)
