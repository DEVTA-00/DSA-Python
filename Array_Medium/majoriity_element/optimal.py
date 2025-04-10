def majorityOptimal(arr:list , n:int):
    count = 0
    for i in range(n):
        if count == 0:
            element = arr[i]
            count = 1
            
        elif arr[i] == element:
            count += 1
        
        else:
            count -= 1
            
    count1 = 0
    for i in range(n):
        if arr[i] == element:
            count1 += 1
    
    if count1 > len(arr) // 2:
        return element
    
    return -1   

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))    
    n = len(arr)
    result = majorityOptimal(arr,n)
    print(result)