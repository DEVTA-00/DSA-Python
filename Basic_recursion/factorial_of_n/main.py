def factorial_n(n):
    if n == 0:
        return 1
    return n * factorial_n(n-1)

n = int(input("Enter the number n: "))
print(factorial_n(n))