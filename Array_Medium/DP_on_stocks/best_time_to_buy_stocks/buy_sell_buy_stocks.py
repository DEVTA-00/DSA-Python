import os

def buy_sell_buy_stocks(arr : list, n : int):
    mini = arr[0]
    maxProfit = 0
    for i in range(1,n):
        cost = arr[i] - mini
        maxProfit = max(maxProfit,cost)
        mini = min(mini,arr[i])
    return maxProfit

if __name__ == "__main__":
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")

    with open(input_file, "r") as file:
        content = file.read().strip()
        arr = list(map(int,content.split()))
        n = len(arr)

        result = buy_sell_buy_stocks(arr, n)
        print(f"Input array: {arr}")
        print(f"Best time to buy and sell stocks: {result}")
