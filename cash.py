from cs50 import get_float
from math import floor

def main():
    n = get_good_float("Change owed: ")

    cents = floor(100 * n)

    a = cents // 25
    b = (cents % 25) // 10
    c = ((cents % 25) % 10) // 5
    d = (((cents % 25) % 10) % 5) // 1

    print(f"{a+b+c+d:.0f}")

def get_good_float(promt):
    while True:
        g = get_float(promt)
        if g > 0:
            break
    return g

if __name__ == "__main__":
    main()
