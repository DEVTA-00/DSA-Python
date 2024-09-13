def print1_n(n):
    if n > 0:
        print1_n(n-1)
        print(n)
    return

if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    print1_n(n)
    