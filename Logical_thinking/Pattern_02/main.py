# *
# **
# ***
# ****
# *****
def pattern2(n):
    
    for i in range(n):
        for j in range(i):
            print('*', end=' ')
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the Number: "))
    pattern2(n)