# *****
# ****
# ***
# **
# *

def pattern5(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end=' ')
        print()

if __name__ == "__main__":
    n = int(input("Enter the number n : "))
    pattern5(n)