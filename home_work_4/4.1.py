null = []
num = 0

for i in range(len(null)):
    if null[i] != 0:
        null[num], null[i] = null[i], null[num]
        num += 1

print(null)
