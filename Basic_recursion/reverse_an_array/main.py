def f(i, arr,n):
    if i>= n/2:
        return
    temp = arr[i]
    arr[i] = arr[n-1-i]
    arr[n-1-i] = temp
    f(i+1, arr, n)

if __name__ == "__main__":      
    arr = list(map(int,input("Enter the array elements: ").split()))
    f(0, arr , len(arr))
    print(arr)