from cs50 import get_int

def main():
    n = get_good_int("Height: ")

    for i in range(n):
        for j in range(n - i - 1):
            print (" ", end="")
        for k in range(i + 1):
            print ("#", end="")
        print("  ", end="")
        for w in range(i + 1):
            print ("#", end="")
        print ("")

def get_good_int(promt):
    while True:
        g = get_int(promt)
        if g > 0 and g < 9:
            break
    return g

if __name__ == "__main__":
    main()
