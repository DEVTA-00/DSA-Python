#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

def pattern9(n):

    for i in range(n):
        for j in range(n-i-1):
            print('.', end=" ")
        for k in range(2*i+1):
            print('*',end=" ")
        for l in range(n-i-1):
            print('.',end=" ")
        print()
    for i in range(n,0,-1):
        # space
        for j in range(n-i):
            print('.',end=" ")
        # star
        for k in range(2*i-1):
            print('*',end=" ")
        # space
        for l in range(n-i):
            print('.',end=" ")
        print() 
    
        
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern9(n)