def missing_number(arr,n):
    # arr = [1,2,4,5]
    # n = 5
    for i in range(1,n+1):
        flag = 0
        for j in range(n):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
    
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = missing_number(arr,n)
    print(result)
    # print(missing_number())