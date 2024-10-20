user_array = list(map(int,input("Enter the user_array: ").split()))
length = len(user_array)

max = 0
for i in range(length):
    if user_array[i] > max:
        max = user_array[i]
        
# precompute
default_value = 0
size = max + 1
hash_map = [default_value] * size
for i in range(length):
    hash[user_array[i]] += 1
    