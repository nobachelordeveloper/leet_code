def is_palindrome_permutation(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Create a dictionary to store character counts
    char_count = {}
    
    # Count the occurrence of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Count the number of characters with odd counts
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    # If there's more than one character with odd count, it cannot form a palindrome
    return odd_count <= 1

# Test the function
print(is_palindrome_permutation("Tact Coa"))  # Output: True
