def findNumberOccursOnce(arr:list , n:int):
    hash_map = {}
    for array_index in range(n):
        array_element = arr[array_index]
        if array_element in hash_map:
            hash_map[array_element] += 1
        else:
            hash_map[array_element] = 1
            
    print(hash_map)
    
    for hash_key in hash_map:
        if hash_map[hash_key] == 1:
            return hash_key
    
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = findNumberOccursOnce(arr,n)
    print(result)       