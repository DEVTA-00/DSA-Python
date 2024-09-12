n = int(input("Enter the number n: "))
def print1(n):
    revNum = 0
    dup = n
    while(n > 0):
        ld = int(n % 10)
        revNum = (revNum * 10) + ld
        n = int(n / 10)
    if dup == revNum:
        print(True)
    else:
        print(False)
        
print1(n)
        

    
