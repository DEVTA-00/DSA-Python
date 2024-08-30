#       A
#     A B A 
#   A B C B A 
# A B C D C B A 

def pattern17(n):
    for i in range(n):
        breakpoint = (2*i+1)/2
        start = 64
        for j in range(n-i-1):
            print(' ',end=" ")
        for k in range(2*i+1):
            if k <= breakpoint:
                start += 1
                print(chr(start),end = " ")
            else:
                start -= 1
                print(chr(start),end=" ")
        for l in range(n-i-1):
            print(' ',end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern17(n)
    
    