def optimalTwoSum(arr:list , n:int , target:int):
    sorted_arr = sorted(arr)
    left = 0
    right = n - 1
    
    while left < right:
        sum = sorted_arr[left] + sorted_arr[right]
        
        if sum == target:
            return "YES"
        elif sum < target:
            left += 1
        else:
            right -= 1
    return "NO"

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    target = 15
    result = optimalTwoSum(arr,n,target)
    print(result)