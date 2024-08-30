# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *    

def pattern19(n):
    inispaces = 0
    for i in range(n):
        # stars
        for j in range(n-i):
            print('*', end=" ")
        # spaces
        for k in range(inispaces):
            print(' ',end=" ")
        # stars
        for l in range(n-i):
            print('*', end=" ")
        inispaces+=2
        print()
    inispaces = 8
    for m in range(n):
        # stars
        for q in range(m+1):
            print('*', end=" ")
        # spaces
        for o in range(inispaces):
            print(' ',end=" ")
        # stars
        for p in range(m+1):
            print('*', end=" ")
        inispaces-=2
        print()
    
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern19(n)