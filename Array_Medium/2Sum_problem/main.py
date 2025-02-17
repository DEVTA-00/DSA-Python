def twoSum(arr:list , n:int , target:int):
    for i in range(n):
        for k in range(i+1,n):
            if arr[i] + arr[k] == target:
                return [i,k]
            
            
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    target = int(input("Enter the sum: "))
    result = twoSum(arr,n,target)
    print(result)