def selection_sort(arr):
    for i in range(len(arr)):
        min_element_index = i
        for k in range(i + 1,len(arr)):
            if arr[k] < arr[min_element_index]:
                temp = arr[k]
                arr[k] = arr[min_element_index]
                arr[min_element_index] = temp
    return arr
                           
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array elements: ").split()))
    print("Array before sorting: ",arr)
    result = selection_sort(arr)
    print("Array after sorting: ",result)
    