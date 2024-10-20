user_string = input("Enter a string: ")
user_string = user_string.lower()
length = len(user_string)

# precompute
default_value = 0
hash_array = [default_value] * 26
for i in range(length):
    hash_array[ord(user_string[i])-ord("a")] += 1
    
# query inputs
queries = list(map(str,input("Enter the number of queries: ").split()))
for query in queries:
    print(hash_array[ord(query)-ord("a")])