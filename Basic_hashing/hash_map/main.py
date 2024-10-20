user_array = list(map(int,input("Enter the user_array: ").split()))

# precompute
hash_map = {}
for element in user_array:
    if element in hash_map:
        hash_map[element] += 1
    else:
        hash_map[element] = 1
        
# taking user query
user_query = list(map(int,input("Enter the user_array: ").split()))
for query in user_query:
    if query in hash_map:
        print(f"the occurence of {query} is {hash_map[query]}")
    else:
        print(f"the occurence of {query} is {0}")
        