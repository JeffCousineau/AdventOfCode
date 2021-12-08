import numpy as np

def fast_func(array, nb_days):
    np_array = np.array(array)
    for day in range(nb_days):
        np_array = np_array - 1
        new_fish = np.count_nonzero(np_array == -1)
        np_array[np_array == -1] = 6
        np_array = np.pad(np_array, (0,new_fish), 'constant', constant_values=(8))
    print(len(np_array))

if __name__ == "__main__":
    f = open("input.txt", "r")
    data = []
    for i in f.readline().split(","):
        data.append(int(i)) 
    fast_func(data,80)