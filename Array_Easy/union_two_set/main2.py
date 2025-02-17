def union(arr1,arr2):
    m = 0
    n = 0
    a1 = len(arr1)
    a2 = len(arr2)
    union_array = []
    
    arr1.sort()
    arr2.sort()
    
    while m < a1 and n < a2:
        if arr1[m] < arr2[n]:
            if len(union_array) == 0 or arr1[m] != union_array[-1]:
                union_array.append(arr1[m])
            m += 1
        else:
            if len(union_array) == 0 or arr2[n] != union_array[-1]:
                union_array.append(arr2[n])
            n += 1
    
    while m < a1:
        if len(union_array) == 0 or arr1[m] != union_array[-1]:
            union_array.append(arr1[m])
        m += 1
        
    while n < a2:
        if len(union_array) == 0 or arr2[n] != union_array[-1]:
            union_array.append(arr2[n])
        n += 1
            
    return union_array

if __name__ == "__main__":
    arr1 = list(map(int,input("Enter the array1: ").split()))
    arr2 = list(map(int,input("Enter the array2: ").split()))
    result = union(arr1,arr2)
    print(result)

