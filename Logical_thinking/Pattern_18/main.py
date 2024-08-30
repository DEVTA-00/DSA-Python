# E 
# D E 
# C D E 
# B C D E 
# A B C D E 

def pattern18(n):
    start = 69
    for i in range(n):
        for j in range(start-i,start+1):
            print(chr(j),end=" ")
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern18(n)

            
        
