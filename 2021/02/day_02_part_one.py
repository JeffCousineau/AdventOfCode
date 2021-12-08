f = open("input.txt", "r")
pos = 0
depth = 0

for line in f:
    if line.split(" ")[0] == "forward":
        pos += int(line.split(" ")[1])
    elif line.split(" ")[0] == "up":
        depth -= int(line.split(" ")[1])
    elif line.split(" ")[0] == "down":
        depth += int(line.split(" ")[1])
    #print(pos, depth)

print(pos * depth)