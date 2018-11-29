import random

SIZE = 20


def main():
    pinakas = [random.randint(0, 100) for i in range(SIZE)]
    print("Arxikos pinakas.")
    print_array(pinakas, SIZE)

    pinakas = bubble_sort(pinakas, SIZE)
    print("O neos pinakas.")
    print_array(pinakas, SIZE)

    print("Press any key to continue", end = "... ")
    input()

    return 1


def print_array(pinakas, n):
    print("[ ", end='')
    for i in range(n - 1):
        print(pinakas[i], end=", ")
    print(pinakas[n-1], "]", end='\n')


def bubble_sort(pinakas, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if pinakas[j] < pinakas[j-1]:
                pinakas[j], pinakas[j-1] = pinakas[j-1], pinakas[j]
        print("Bhma  ", i+1, end = " : ")
        print_array(pinakas, n)

    return pinakas


if __name__ == "__main__":
    main()
