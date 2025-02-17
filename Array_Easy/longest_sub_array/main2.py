def longestSubArray(arr:list , k:int , n:int):
    left = 0
    right = 0
    sum = arr[0]
    max_len = 0
    
    while (right < n):
        while left <= right and sum > k:
            sum -= arr[left]
            left += 1
            
        if sum == k:
            max_len = max(max_len , right - left + 1)
   
        right += 1
        if right < n:
            sum += arr[right]
            
    return max_len

if __name__ == "__main__":
    arr = [1 , 2 , 3 , 1 , 1 , 1 , 1 , 3 , 3]
    n = len(arr)
    k = 6
    result = longestSubArray(arr,k,n)
    print(result)
