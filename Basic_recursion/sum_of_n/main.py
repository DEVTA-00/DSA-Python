def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)
      
n = int(input("Enter the number n: "))
print("The sum of first n numbers: ",sum_n(n))
sum_n(n)

# def sum_n(n):
#     total_sum = 0
#     for i in range(n+1):
#         total_sum += i
#     return total_sum

        
        
# n = int(input("Enter the number n: "))
# print("The sum of n numbers: ",sum_n(n))
# sum_n(n)

