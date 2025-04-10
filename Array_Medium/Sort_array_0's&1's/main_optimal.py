def optimalSort(arr:list , n:int):
    low = 0
    mid = 0 
    high = n - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

if __name__ ==  "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = optimalSort(arr,n)
    print(result)