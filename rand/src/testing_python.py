from file_reader import FileReader

print(__name__)

fr = FileReader()

print(fr.read("data/file_reader_test1.txt"))

data = fr.read_as_str_lines("data/test2.txt")

for line in data:
    print('line: ' + line)

data2 = fr.read_as_int_lines("data/2020_test1.txt")
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
