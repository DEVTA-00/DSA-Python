def moveNonZeros(arr,n):
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
            
    for i in range(len(temp)):
        arr[i] = temp[i]
        
    noOfNonZeros = len(temp)
    for i in range(noOfNonZeros,n):
        arr[i] = 0
        
    return arr
        
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = moveNonZeros(arr,n)
    print(result)