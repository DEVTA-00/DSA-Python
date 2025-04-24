import sys
import os

def maximum_subArray_sum (arr:list, n:int):
    
    maxi = -sys.maxsize - 1
    
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            maxi = max(sum, maxi)
    return maxi
                
if __name__ == "__main__":

    # Determine the current directory and input file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")

    # Read the input file and parse the array
    with open(input_file, "r") as file:
        content = file.read().strip()
        arr = list(map(int, content.split()))
        n = len(arr)

        # Find and print the maximum subarray sum
        result = maximum_subArray_sum(arr, n)
        print(f"Input array: {arr}")
        print(f"maximum subarray sum: {result}")
    