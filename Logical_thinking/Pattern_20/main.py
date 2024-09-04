# *                 *  
# * *             * * 
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * * 
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

def pattern20(n):
    spaces = 2*n
    for i in range(2*n):
        stars = i
        if(i>n):
            stars = 2*n-i
        # stars
        for j in range(stars):
            print('*',end=" ")
        # spaces
        for k in range(spaces): 
            print(' ',end=" ")   
        # stars
        for l in range(stars):
            print('*',end=" ")
        if(i<n):
            spaces -= 2
        else:
            spaces += 2
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern20(n)