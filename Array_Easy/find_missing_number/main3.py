def missingNumber(arr:list,k:int,n:int):
    sum = n*(n+1) // 2
    arr_sum = 0
    for i in range(k):
        arr_sum += arr[i]
    return (sum - arr_sum)

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    k = len(arr)
    n = int(input("Enter the number n : "))
    result = missingNumber(arr,k)
    print(f"The missing number is: {result}")