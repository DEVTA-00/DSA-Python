def appearsOnce(arr:list,n:int):
    XOR = 0
    for i in range(n):
        XOR = XOR ^ arr[i]
    return XOR

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    n = len(arr)
    result = appearsOnce(arr,n)
    print(result)