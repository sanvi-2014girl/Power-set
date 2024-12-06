import math
def printPowerSet(input_set,set_size):
    power_set_size = (int(math.pow(2, set_size)))
    outer = 0
    inner = 0
for outer in range(power_set_size):
    for inner in range(set_size):
        if((outer & (1 << inner)) > 0):
            print(set[inner], end = "")
    print("")
size = int(input("Enter array size: "))
input_size = []
for i in range(0,size):
    n = int(input("Enter element: "))
    set.append(n)
printPowerSet(input_set, len(input_set))
