def leftRotate(arr,n):
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr
    
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    result = leftRotate(arr,len(arr))
    print(result)
    