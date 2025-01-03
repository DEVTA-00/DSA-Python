def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        didswap = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                didswap = 1
                print(arr)
        if didswap == 0:
            break
    return arr



if __name__ == "__main__":
    arr = list(map(int,input("Enter the array elements: ").split()))
    print("Array before sorting: ",arr)
    result = bubble_sort(arr)
    print("Array after sorting: ",result)
    