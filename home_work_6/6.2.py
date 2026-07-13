num = int(input('Введіть число:'))
if num < 0 or num > 8640000:
    print("Помилка! Введіть число більше за '0' та менше за '8640000.'")
else:

    days, remainder = divmod(num, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days % 10 == 1 and days % 100 != 11:
        word = "день"
    elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
        word = "дні"
    else:
        word = "днів"

    hours_format = str(hours).zfill(2)
    minutes_format = str(minutes).zfill(2)
    seconds_format = str(seconds).zfill(2)

    print(f'{days} {word}, {hours_format}:{minutes_format}:{seconds_format}')
