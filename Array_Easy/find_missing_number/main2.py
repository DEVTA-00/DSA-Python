def missing_number(arr,array_length):
    hash = [0]*(array_length+2)
    
    
    for array_index in range(array_length):
        print(hash)
        hash[arr[array_index]] = 1
        print(hash)
        
    for hash_array_index in range(1,array_length):
        if hash[hash_array_index] == 0:
            return hash_array_index
        
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    array_length = len(arr)
    result = missing_number(arr,array_length)
    print(result)