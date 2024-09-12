n = int(input("Enter the number n: "))
def print3(n):
    for i in range(n):
        if n % (i+1) == 0:
            print(i+1,end=",")
            
print3(n)

# import math
# def print4(n):
#     for i in range(int(math.sqrt(n))):
#         if n % (i+1) == 0:
#             my_list.append(i+1)
#             if(n/(i+1)) != i:
#                 my_list.append(int(n/(i+1)))
                
# n = int(input("Enter the number n: "))
# my_list = []
    
# print4(n)
# my_list.sort()
# print(my_list)
