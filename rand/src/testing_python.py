from file_reader import FileReader

print(__name__)

fr = FileReader()

data2 = fr.read_as_int_lines("../data/2020_test1.txt")
total = 0
for num in data2:
    print('num: ' + str(num))
    total += num
    print('total: ' + str(total))

data2.sort()
for num in data2:
    print('num: ' + str(num))

# 2020 day 1 test
for i, val_i in enumerate(data2):
    print(str(i) + '-' + str(val_i))
    for y, val_y in reversed(list(enumerate(data2))):
        # print('--' + str(y) + '-' + str(valy))
        if val_i + val_y == 2020:
            print('FOUND: ' + str(val_i) + ' + ' + str(val_y))
            break
        if val_i + val_y < 2020:
            # print('LESS')
            break
        if i == y:
            break

# day1 solve by other
d = [*map(int, open("../../data/day1_in.txt", 'r'))]
p1 = sum(map(int.__gt__, d[1:], d))
print("problem 1: " + str(p1))

# test reference list and lambdas
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('h: ' + str(a[3:]))

tsr = ['1', '2', '3', '4']
print(*map(int, tsr))
print(tsr)
print(*tsr)

tsr2 = map(int, tsr)
print(*map(lambda x: x * x, tsr2))
