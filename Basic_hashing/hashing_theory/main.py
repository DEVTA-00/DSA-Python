arr = list(map(int,input("Enter the array elements: ").split()))
length = len(arr)

# precompute
max = 0
for i in range(length):
    if arr[i] > max:
        max = arr[i]

# creating hashing
default_value = 0
size = max + 1
hash = [default_value] * size

# hashing
for i in range(length):
    hash[arr[i]] += 1
    
user_array = list(map(int,input("Enter the elements of the user array: ").split()))
    
# fetch
for i in range(len(user_array)):
    if user_array[i] > max:
        print(f"The frequency of {user_array[i]} is 0")
    else:
        print(f"The frequency of {user_array[i]} is {hash[user_array[i]]}")