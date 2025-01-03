# merge algo
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    
    # Checking if the left pointer exceeds the mid and right pointer exceeds high
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1       
        else:
            temp.append(arr[right])
            right += 1
              
    while left <= mid:
        temp.append(arr[left])
        left += 1
        
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low,high+1):
        arr[i] = temp[i-low]
    
def mS(arr,low,high):
    if(low >= high):
        return
    mid = int((low + high)/2)
    mS(arr,low,mid)
    mS(arr,mid + 1,high)
    merge(arr,low,mid,high)
    
# def mergeSort(arr, n):
#     mS(arr, 0, n-1)
#     return arr
    
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    print(arr)
    n = len(arr)
    mS(arr,0,n-1)
    print(arr)