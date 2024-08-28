# 1
# 22
# 333
# 4444
# 55555

def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=' ')
        print()
        
if __name__== "__main__":
    n = int(input("Enter the number n: "))
    pattern4(n)
    