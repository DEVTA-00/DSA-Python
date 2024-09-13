def print1_n(value,n):
    if value > 0:
        print(value)
        print1_n(value-1,n)
    return

if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    value = n
    print1_n(value,n)
