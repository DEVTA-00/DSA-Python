def maximumConsecutiveOnes(arr:list,n:int):
    count = 0
    max_count = 0
    for i in range(n):
        if arr[i] == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = maximumConsecutiveOnes(arr,n)
    print(result)