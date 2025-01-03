def isSorted(a, n):
    for i in range(1, n):
        if a[i] >= a[i-1]:
            continue
        else:
            return False
    return True

if __name__ == "__main__":      
    arr = list(map(int,input("Enter the array: ").split()))
    result = isSorted(arr, len(arr))
    
    print(result)