# A B C D E 
# A B C D 
# A B C 
# A B 
# A

def pattern15(n):
    for i in range(n):
        start = 64
        for j in range(n-i):
            start += 1
            print(chr(start), end=" ")
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern15(n)