def longestSubarray(arr:list, n:int):
    for i in range(n):
        for k in range(i,n):
            sum = 0
            for m in range(i,k):
                sum += arr[m]
                