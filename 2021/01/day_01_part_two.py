f = open("input.txt", "r")
i = 0
count = 0
last = -1
lines_table = []
for x in f:
    lines_table.append(int(x))
try:
    for x in range(0, len(lines_table)):
        print(lines_table[x],lines_table[x+1],lines_table[x+2])
        sum = lines_table[x] + lines_table[x+1] + lines_table[x+2]
        if sum > last and last != -1:
            count += 1
        last = sum
except:
    print("end of file")
    print(count)
    f.close()