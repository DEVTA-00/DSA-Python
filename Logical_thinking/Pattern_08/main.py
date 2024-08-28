# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *



def pattern8(n):
    for i in range(n,0,-1):
        # space
        for j in range(n-i):
            print(' ',end=" ")
        # star
        for k in range(2*i-1):
            print('*',end=" ")
        # space
        for l in range(n-i):
            print(' ',end=" ")
        print()
        
        
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern8(n)