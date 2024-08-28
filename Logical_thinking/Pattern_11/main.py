# 1 
# 0 1
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 

def pattern11(n):
    start = 1
    for i in range(n):
        if(i%2 == 0):
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(start, end=" ")
            start = 1-start
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern11(n)