# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def pattern13(n):
    start = 0
    for i in range(n):
        for j in range(i+1): 
            start = start + 1 
            print(start, end = " ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern13(n)