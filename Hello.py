import os

def list_func(*pinakas):
    pinakas.append = "alla3e"

def main():
    x = 9 + 6
    y = 5 + 9
    z = x + y
    phrase = "Hello World!"
    print(phrase.replace("Hello", "Hi"))
    print(z, '\n')

    pinakas = [0, 1, 2]
    list_func(pinakas)

    print(pinakas)

    os.system("pause")

    return 1

if __name__ == "__main__":
    main()