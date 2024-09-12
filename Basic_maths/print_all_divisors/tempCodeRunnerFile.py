n = int(input("Enter the number n: "))
def print3(n):
    for i in range(n):
        if n % (i+1) == 0:
            print(i+1)
            
print3(n)