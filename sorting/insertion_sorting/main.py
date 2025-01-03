def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr
            
if __name__ == "__main__":
    arr = list(map(int,input("Enter th array elements:").split()))
    print("Before sorting: ",arr)
    result = insertion_sort(arr)
    print("After sorting: ",result)