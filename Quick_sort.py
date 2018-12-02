import random
import os

def quickSort(pinakas):
    less = []
    equal = []
    greater = []
    if len(pinakas) > 1:
        pivot = pinakas[0]
        for x in pinakas:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)
    return pinakas

def printArray(pinakas):
    print("[ ", end='')
    for i in range(len(pinakas) - 1):
        print("%2d" % pinakas[i], end=", ")
    print(pinakas[len(pinakas) - 1], "]", end='\n')


def init_array(n):
    pinakas = []
    for i in range(n):
        pinakas.append(random.randint(0, 100))
    return pinakas

def main():
    SIZE = 7
    pinakas = []
    pinakas = init_array(SIZE)
    print("Arxikos pinakas", end=": ")
    printArray(pinakas)

    pinakas = quickSort(pinakas)
    print("O neos pinakas:")
    printArray(pinakas)


if __name__ == "__main__":
    main()
