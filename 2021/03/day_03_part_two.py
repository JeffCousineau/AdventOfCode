def binstr_to_int(string):
    return int(string, base=2)
 
def get_gamma_rate(table):
    count = []
    for i in range(0, len(table[0])-1):
        count.append(0)
    for line in table:
        for i in range(0, len(line)):
            if line[i] == '1':
                count[i] += 1
    binary_number = '0b'
    for i in count:
        if i > len(table)/2:
            binary_number+= '1'
        else:
            binary_number+= '0'
    return binary_number

def get_epsilon_rate(table):
    count = []
    for i in range(0, len(table[0])-1):
        count.append(0)
    
    for line in table:
        for i in range(0, len(line)):
            if line[i] == '1':
                count[i] += 1
    binary_number = '0b'
    for i in count:
        if i < len(table)/2:
            binary_number+= '1'
        else:
            binary_number+= '0'
    return binary_number

# Return [count of 0, count of 1]
def get_bit_count(table, index):
    count = [0,0]
    for line in table:
        if list(line)[index] == '0':
            count[0] += 1
        else:
            count[1] += 1
    return count

def get_oxygen_generator_rating(table):
    for bit in range(0,len(table[0])):
        bit_count = get_bit_count(table, bit)
        most_common = 1
        if bit_count[0] > bit_count[1]:
            most_common = 0
        print(bit_count, " most commmon : ", most_common, table)
        new_table = []
        for line in table:
            if int(list(line)[bit]) == most_common:
                new_table.append(line)
            else:
                print("Removing " + str(line) + " because of bit " + str(bit) + " being " + str(list(line)[bit]))
        table = new_table
        print("New table : ", table)
        if len(table) == 1:
            return binstr_to_int(table[0])

def get_co2_scrubber_rating(table):
    for bit in range(0,len(table[0])):
        bit_count = get_bit_count(table, bit)
        least_common = 0
        if bit_count[0] > bit_count[1]:
            least_common = 1
        print(bit_count, " most commmon : ", least_common, table)
        new_table = []
        for line in table:
            if int(list(line)[bit]) == least_common:
                new_table.append(line)
            else:
                print("Removing " + str(line) + " because of bit " + str(bit) + " being " + str(list(line)[bit]))
        table = new_table
        print("New table : ", table)
        if len(table) == 1:
            return binstr_to_int(table[0])

if __name__ == "__main__":
    f = open("input.txt", "r")

    gamma_rate_bin = 0
    epsilon_rate_bin = 0

    data = []
    for line in f:
        data.append(line.removesuffix('\n'))
    print(data)

    oxygen_rating = get_oxygen_generator_rating(data)
    co2_rating = get_co2_scrubber_rating(data)
    print("Oxygen rating", oxygen_rating)
    print("CO2 rating", co2_rating)
    print("Life support rating", oxygen_rating * co2_rating)