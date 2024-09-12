n = int(input("Enter the number n: "))
def print2(n):
    armstrong = 0
    dup = n
    while(n > 0):
        ld = int(n % 10)
        armstrong = int(ld*ld*ld) + armstrong
        n = int(n / 10)
        
    if armstrong == dup:
        print(True)
    else:
        print(False)
            
print2(n)
        