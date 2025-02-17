def moveNonZeros(arr,n):
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    
    for i in range(j+1,n):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
            
    return arr
    
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = moveNonZeros(arr,n)
    print(result)