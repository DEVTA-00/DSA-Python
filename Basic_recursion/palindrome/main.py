def is_palindrome(i, userInput):
    if i >= len(userInput) // 2:
        return True
    if userInput[i] != userInput[len(userInput)-i-1]:
        return False
    return is_palindrome(i+1, userInput)
    
if __name__ == "__main__":
    userInput = input("Enter a string: ")
    userInput = userInput.upper()
    print(is_palindrome(0, userInput))