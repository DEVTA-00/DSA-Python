def longestSubarray(arr:list,n:int):
    sum = 0
    maxlen = 0
    for i in range(n):
        sum += arr[i]
        if sum == n:
            maxlen = max(maxlen)