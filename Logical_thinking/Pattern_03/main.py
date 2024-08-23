# 1
# 1 2
# 1 2 3
# 1 2 3 4

def pattern3(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=' ')
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the Number of n: "))
    pattern3(n)