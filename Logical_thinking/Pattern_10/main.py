# *
# * *
# * * *
# * * * * 
# * * * * *
# * * * *
# * * *
# * *
# *

def pattern10(n):
    for i in range(2*n-1):
        star = i+1
        # print(i)
        if(i>=n):
            star = 2*n-i-1
        for j in range(star):
            print('*', end=" ")
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the number n: "))
    pattern10(n)
    
    
# def pattern10(n):
#     for i in range(n*2):
#         if i>n:
#             for j in range((2*n)-i+1):
#                 print('*',end=" ")
#             for k in range((2*n)+i+1):
#                 print(' ',end=" ")      
#         else:
#             for j in range(i+1):
#                 print('*', end=" ")
#             for k in range(n-i):
#                 print(' ',end=" ")
#         print("\n")

# if __name__ == "__main__":
#     n = int(input("Enter the number n: "))
#     pattern10(n)

