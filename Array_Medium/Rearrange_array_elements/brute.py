import os

def rearrangeArrayEle(arr : list, n : int):
    positive = []
    negative = []

    for i in range(n):
        if arr[i] > 0:
            positive.append(arr[i])
        else:
            negative.append(arr[i])

    # for i in range(len(positive)):
    #     arr[2 * i] = positive[i]

    # for i in range(len(negative)):
    #     arr[2 * i + 1] = negative[i]
    
    for i in range(n//2):
        arr[2 * i] = positive[i]
        arr[2 * i + 1] = negative[i]
            
    return arr

    
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")

    with open(input_file, "r") as file:
        content = file.read().strip()
        arr = list(map(int, content.split()))
        n = len(arr)

        result = rearrangeArrayEle(arr, n)
        print(f"Input Array: {arr}")
        print(f"After Rearrange array elements: {result}")