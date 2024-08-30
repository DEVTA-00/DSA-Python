# A
# A B 
# A B C 
# A B C D 
# A B C D E 

def pattern14(n):
    for i in range(n):
        start = 64 
        for j in range(i+1):
            start += 1
            print(chr(start), end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern14(n)