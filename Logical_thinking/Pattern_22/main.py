# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

def pattern22(n):
    for i in  range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            right = (2*n-2)-j
            down = (2*n-2)-i
            print(n-min([min([top,down]),min([left,right])]),end=" ")
        print()
    
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern22(n)