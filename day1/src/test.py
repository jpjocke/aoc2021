from util.FileReader import FileReader

fr = FileReader()

print(fr.read("./data/test1.txt"))

data = fr.read_as_str_lines("./data/test2.txt")

for line in data:
    print('line: ' + line)

data2 = fr.read_as_int_lines("./data/test3.txt")
total = 0
for num in data2:
    print('num: ' + str(num))
    total += num
    print('total: ' + str(total))