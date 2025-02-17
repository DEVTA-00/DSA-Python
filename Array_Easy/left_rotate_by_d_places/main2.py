# optimal_method
def reverse(arr,start,end):
    while(start <= end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
        
def rotateLeftToRight(arr,n,d):
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    
    return arr
    
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    d = int(input("Enter the value of d: "))
    n = len(arr)
    result = rotateLeftToRight(arr,n,d)
    print(result)