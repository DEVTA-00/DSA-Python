import os

def rearrangeArray(arr:list , n:int):
    ans = [0] * n
    
    posIndex , negIndex = 0,1
    for i in range(n):
        if arr[i] < 0:
            ans[negIndex] = arr[i]
            negIndex += 2
            
        else:
            ans[posIndex] = arr[i]
            posIndex += 2
            
    return ans

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")
    
    with open(input_file, "r") as file:
        content = file.read().strip()
        arr = list(map(int, content.split()))
        n = len(arr)

        result = rearrangeArray(arr, n)
        print(f"Input Array: {arr}")
        print(f"After RearrangeArray: {result}")