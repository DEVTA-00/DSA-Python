def findElementAppersOnce(arr:list,n:int):
    for i in range(n):
        num = arr[i]
        count = 0
        for k in range(n):
            if arr[k] == num:
                count += 1
        if count == 1:
            return num

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = findElementAppersOnce(arr,n)
    print(result)