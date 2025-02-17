def leftRotate(arr,n,d):
    d = d % n
    
    # store values
    temp = []
    # put into the array
    for i in range(d):
        temp.append(arr[i])
        print(temp)
    
    # shifting
    for k in range(d,n):
        arr[k-d] = arr[k]
    
    # pushback   
    for p in range(n-d,n):
        arr[p] = temp[p-(n-d)]
        
    return arr
        
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    d = int(input("Enter the value of d: "))
    n = len(arr)
    result = leftRotate(arr,n,d)
    print(*result)