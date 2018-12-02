import random

SIZE = 20


def print_array(pinakas, n):
    print("[ ", end='')
    for i in range(n - 1):
        print("%3d" % pinakas[i], end=", ")
    print(pinakas[n-1], "]", end='\n')


def init_array(pinakas, n):
    pinakas = []
    for i in range(n):
        pinakas.append(random.randint(0, 100))
    return pinakas


def merge_sort(pinakas):
    merge_sort2(pinakas, 0, len(pinakas) - 1)


def merge_sort2(pinakas, start, finish):
    if start == finish:
        return
    elif start == finish - 1:
        if pinakas[start] > pinakas[finish]:
            pinakas[start], pinakas[finish] = pinakas[finish], pinakas[start]
    else:
        middle = (start + finish) // 2

        merge_sort2(pinakas, start, middle)
        merge_sort2(pinakas, middle + 1, finish)
        merge(pinakas, start, middle, finish)

def merge(pinakas, start, middle, finish):
    C = list(pinakas)
    k = start
    i = start
    n = middle

    j = middle + 1
    m = finish

    while (i<=n and j <= m):
        if C[i] <= C[j]:
            pinakas[k] = C[i]
            i += 1
            k += 1
        else:
            pinakas[k] = C[j]
            j += 1
            k += 1
    
    if i > n:
        while j <= m:
            pinakas[k] = C[j]
            j += 1
            k += 1
    else:
        while i <= n:
            pinakas[k] = C[i]
            i += 1
            k += 1
        


def main():
    pinakas = []
    pinakas = init_array(pinakas, SIZE)
    print("Arxikos pinakas", end=": ")
    print_array(pinakas, SIZE)

    merge_sort(pinakas)
    print("O neos pinakas:")
    print_array(pinakas, SIZE)


if __name__ == "__main__":
    main()
