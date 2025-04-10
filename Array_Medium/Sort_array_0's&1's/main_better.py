def betterSort(arr:list , n:int):
    count0 = 0
    count1 = 0
    count2 = 0
    
    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
        
    for i in range(count0):
        arr[i] = 0
    for i in range(count0,(count0 + count1)):
        arr[i] = 1
    for i in range((count0 + count1) ,n):
        arr[i] = 2
    return arr
        
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = betterSort(arr,n)
    print(result)