import numpy as np

# Keep a count of number of fish with X ammount of days left
# ex: [0,0,0,1,1,2,3,3,3,3,4,5,6,6] => [3,2,1,4,1,1,2]
def count_fish_by_age(array, max_age):
    new_array = [0]*(max_age+1)
    for i in array:
        new_array[i] += 1
    return new_array

def new_day(array, nb_days):
    for day in range(nb_days):
        new_fish = array[0]
        array.pop(0)
        array.append(new_fish)
        array[6] += new_fish
    return sum(array)

if __name__ == "__main__":
    f = open("input.txt", "r")
    data = []
    for i in f.readline().split(","):
        data.append(int(i)) 
    fish_count = count_fish_by_age(data, 8)
    print(new_day(fish_count, 256))