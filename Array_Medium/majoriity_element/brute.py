def majorityElementBrute(arr:list , n:int):
    for i in range(n):
        count = 0
        for k in range(n):
            if arr[k] == arr[i]:
                count += 1
        if count > n//2:
            return arr[i]
    return -1

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = majorityElementBrute(arr,n)
    print(result)