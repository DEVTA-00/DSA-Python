def findTheNumberOnceAppearsBetter(arr:list,n:int):
    max_element = 0
    for i in range(n):
        if arr[i] > max_element:
            max_element = arr[i]

    hash_array = [0] * (max_element+ 1)
    # print(hash_array)
    for i in range(n):
        hash_array[arr[i]] += 1
    
    # missing_elements = []
    for i in range(len(hash_array)):
        if hash_array[arr[i]] == 1:
            return i
            # missing_elements.append(i)
    # return missing_elements
   
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = findTheNumberOnceAppearsBetter(arr,n)
    print(result)