def common_elements():
    return set(range(0, 100, 3)).intersection(set(range(0, 100, 5)))


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ok')
