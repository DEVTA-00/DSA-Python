import math

def prime(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if((n%i==0)):
            count = count+1
            if(int(n/i) != (i)):
                count = count+1
    if(count == 2):
        print(True)
    else:
        print(False)
        
n = int(input("Enter the number n: "))
prime(n)