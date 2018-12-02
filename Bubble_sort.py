import random
import os


SIZE = 20


def main():
    pinakas = []
    for i in range(SIZE):
        pinakas.append(random.randint(0, 100))
    print("Arxikos pinakas.")
    print_array(pinakas, SIZE)

    pinakas = bubble_sort(pinakas, SIZE)
    print("O neos pinakas.")
    print_array(pinakas, SIZE)

    print()
    os.system("pause")

    return 0


def print_array(pinakas, n):
    print("[ ", end='')
    for i in range(n - 1):
        print("%3d"%pinakas[i], end=", ")
    print(pinakas[n-1], "]", end='\n')


def bubble_sort(pinakas, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if pinakas[j] < pinakas[j-1]:
                pinakas[j], pinakas[j-1] = pinakas[j-1], pinakas[j]
        print("Bhma %2d"%(i), end = " : ")
        print_array(pinakas, n)

    return pinakas


if __name__ == "__main__":
    main()
