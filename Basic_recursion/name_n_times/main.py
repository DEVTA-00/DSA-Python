def print5(count):
    if count < n:
        print("name")
        count += 1
        print5(count)
    return
        
if __name__ == "__main__":
    count = 0
    n = int(input("Enter the number n: "))
    print5(count)