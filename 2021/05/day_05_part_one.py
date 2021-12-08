import numpy as np

if __name__ == "__main__":
    f = open("input.txt", "r")

    data = []
    for line in f:
        line = line.strip('\n').strip(' ')
        start = [int(line.split("->")[0].split(",")[0]),int(line.split("->")[0].split(",")[1])]
        data_line = []
        data_line.append(start)
        end = [int(line.split("->")[1].split(",")[0]),int(line.split("->")[1].split(",")[1])]
        data_line.append(end)
        data.append(data_line)
    
    
    max_length = np.amax(data)
    print("Max value:",max)
    
    table = []
    for i in range(0,max_length+1):
        table.append([0]*(max_length+1))
    
    #print(data)
    for line in data:
        # Vertical line
        if line[0][0] == line[1][0]:
            #print(line)
            x = line[0][0]
            start = min(line[0][1],line[1][1])
            end = max(line[0][1],line[1][1])
            for y in range(start,end+1):
                #print(y)
                table[y][x] += 1

        # Horizontal line
        elif line[0][1] == line[1][1]:
            #print(line)
            y = line[0][1]
            start,end = min(line[0][0],line[1][0]),max(line[0][0],line[1][0])
            for x in range(start,end+1):
                #print(x)
                table[y][x] += 1
        # Horizontal line
        # elif line[0][1] == line[1][1]:
        #     #print(line)
        #     start = min(line[0][0],line[1][0])
        #     end = max(line[0][0],line[1][0])
        #     for i in range(start,end+1):
        #         print(i)
        #         table[line[0][0]][i] += 1
    
    #for line in table:
    #    print(line)
    print(np.count_nonzero(np.array(table) >= 2))
