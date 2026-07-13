import keyword
import string

name = input("Введіть ім'я: ")
true_name = set(string.ascii_lowercase + '0123456789_')

if not name:
    print(False)
elif name in keyword.kwlist:
    print(False)
elif "__" in name:
    print(False)
elif name[0].isdigit():
    print(False)
elif not set(name).issubset(true_name):
    print(False)
else:
    print(True)
