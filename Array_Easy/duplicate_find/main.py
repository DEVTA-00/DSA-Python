# good practice-->>

# step1: create an array
# step2: create a func and pass array and array length in parameter
# step3: iterate the array
# step4: select an element and check through the array 
# step5: if selected element = any of the element of the arrray then pop the element
# step6: after popping all the duplicate element return the array


# Question:
# You are given a sorted integer array 'arr' of size 'n'.

# You need to remove the duplicates from the array such that each element appears only once.

# Return the length of this new array

def removeDuplicates(arr , n):
    i = 0
    for j in range(1,n):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i = i+1
    return i+1

if __name__ == "__main__":
    arr = list(map(int,input("Enter the sorted array: ").split()))
    result = removeDuplicates(arr,len(arr))
    print(result)