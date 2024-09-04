# * * * *
# *     *
# *     *
# * * * *

def pattern21(n):
    for i in range(n):
        # stars 
        for j in range(n):
            if i==0 or j == 0 or i == n-1 or j == n-1:
                print('*', end=" ")
            else:
                print(' ', end = " ") 
        print()

if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern21(n)
                
                
            
        