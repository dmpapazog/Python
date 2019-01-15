import random
import os

SIZE = 10


def print_array(pinakas):
    size = len(pinakas)
    print("[", end='')
    for i in range(size - 1):
        print("%3d" % pinakas[i], end=",")
    print("%3d]" % pinakas[size-1])


def bubble_sort(pinakas):
    size = len(pinakas)
    for i in range(size):
        for j in range(size-1, i, -1):
            if pinakas[j] < pinakas[j-1]:
                pinakas[j], pinakas[j-1] = pinakas[j-1], pinakas[j]
        print("Bhma %2d" % (i+1), end=" : ")
        print_array(pinakas)


def array_init(size):
    pinakas = []
    for i in range(size):
        pinakas.append(random.randint(0, 100))
    return pinakas


def main():
    pinakas = array_init(SIZE)

    print("Arxikos pinakas.")
    print_array(pinakas)

    bubble_sort(pinakas)

    space = ' '
    print("\nO neos pinakas.\n" + (10 * space), end='')
    print_array(pinakas)

    print()
    os.system("pause")

    return 0


if __name__ == "__main__":
    main()
