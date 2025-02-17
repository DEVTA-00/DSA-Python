def union(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    my_set = set()
    for i in range(n1):
        my_set.add(arr1[i])
    for i in range(n2):
        my_set.add(arr2[i])
        
    union_array = []
    for element in my_set:
        union_array.append(element)
    return union_array

if __name__ == "__main__":
    arr1 = list(map(int,input("Enter the 1st array: ").split()))
    arr2 = list(map(int,input("Enter the 2nd array: ").split()))
    result = union(arr1,arr2)
    print(result)

        
    