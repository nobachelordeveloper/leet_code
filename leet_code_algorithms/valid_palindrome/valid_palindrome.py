# My Solution
def isPalindrome(self, s: str) -> bool:
    validChars = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"}
    formattedString = ""
    for letter in s:
        if letter.lower() in validChars:
            formattedString += letter.lower()
    return formattedString == formattedString[::-1]

# ChatGPT Solution
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    valid = []
    for i in s:
        if i.isalpha() or i.isdigit():
            valid.append(i)
    return valid == valid[::-1]
