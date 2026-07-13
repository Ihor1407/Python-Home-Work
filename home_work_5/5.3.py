import string

line = input("Введіть рядок: ")
new_line = line.title()
clear_line = ""

for symbol in new_line:
    if symbol not in string.punctuation and symbol != ' ':
        clear_line += symbol

hashtag = "#" + clear_line

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
