# 12345
# 1234
# 123
# 12
# 1

def pattern6(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=' ')
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern6(n)