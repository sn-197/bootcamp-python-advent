# This file is a palindrome checker.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward
# ... (ignoring spaces, punctuation, and capitalization).

def is_palindrome(s):
    # Remove spaces and punctuation, and convert to lowercase
    cleaned = ''.join(c for c in s if c.isalnum()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
if __name__ == "__main__":
    test_string = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(test_string):
        print(f'"{test_string}" is a palindrome.')
    else:
        print(f'"{test_string}" is not a palindrome.')  

        