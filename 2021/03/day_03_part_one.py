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

if __name__ == "__main__":
    f = open("input.txt", "r")

    gamma_rate_bin = 0
    epsilon_rate_bin = 0

    data = []
    for line in f:
        data.append(line)
        
    gamma_rate = get_gamma_rate(data)
    epsilon_rate = get_epsilon_rate(data)
    print(gamma_rate, binstr_to_int(gamma_rate))
    print(epsilon_rate, binstr_to_int(epsilon_rate))
    print("Power:", binstr_to_int(gamma_rate)*binstr_to_int(epsilon_rate))