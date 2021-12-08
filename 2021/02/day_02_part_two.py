f = open("input.txt", "r")
pos = 0
depth = 0
aim = 0

for line in f:
    if line.split(" ")[0] == "forward":
        pos += int(line.split(" ")[1])
        depth += (aim * int(line.split(" ")[1]))
    elif line.split(" ")[0] == "up":
        aim -= int(line.split(" ")[1])
    elif line.split(" ")[0] == "down":
        aim += int(line.split(" ")[1])

print(pos * depth)