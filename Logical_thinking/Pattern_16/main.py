# A
# B B 
# C C C 
# D D D D 
# E E E E E

def pattern16(n):
    start = 64
    for i in range(n):
        start += 1 
        for j in range(i+1):
            print(chr(start),end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern16(n)