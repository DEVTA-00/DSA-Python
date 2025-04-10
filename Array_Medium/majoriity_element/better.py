def betterMajority(arr:list , n:int):
    hash = {}
    for i in range(n):
        if arr[i] not in hash:
            hash[arr[i]] = 1
        else:
            hash[arr[i]] += 1
            
    for key, value in hash.items():
        if value > n // 2:
            return key
        
    return -1

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = betterMajority(arr,n)
    print(result)