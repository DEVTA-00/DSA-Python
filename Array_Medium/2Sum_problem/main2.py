def betterTwoSum(arr:list , n:int , target:int):
    hash_map = {}
    for i in range(n):
        element = arr[i]
        more = target - element
        
        if more in hash_map:
            return [i , hash_map[more]]  #"YES"
        hash_map[arr[i]] = i
    return 0  #"NO"

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    target = int(input("Enter the sum: "))
    result = betterTwoSum(arr,n,target)
    print(result)
