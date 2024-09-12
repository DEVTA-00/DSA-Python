n=int(input("Enter the number n: "))
revNum = 0
while(n > 0):
    ld = int(n % 10)
    revNum = (revNum * 10)+ld
    n = int(n / 10)

print(revNum)