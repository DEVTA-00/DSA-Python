# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1

def pattern12(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")
        for k in range(2*(n-i)-2):
            print('.', end=" ")
        for l in range(i, -1, -1):
            print(l+1, end=" ")
        print()
        
if __name__ == "__main__":
    n = int(input("Ënter the number n: "))
    pattern12(n)