def missingNumber(arr:list,array_len:int):
    XOR1 = 0
    for i in range(1,array_len+2):
        XOR1 = XOR1 ^ i
    XOR2 = 0
    for i in range(array_len):
        XOR2 = XOR2 ^ arr[i]
    return XOR1 ^ XOR2

if __name__== "__main__":
    arr = list(map(int,input("Enter the array: ").split()))
    array_len = len(arr)
    result = missingNumber(arr,array_len)     
    print(f"The missing number is {result}")