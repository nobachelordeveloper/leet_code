def longestPalindrome(self, s: str) -> int:
    letter_tracker = {}
    count = 0
    for letter in s:
        if letter in letter_tracker:
            letter_tracker.pop(letter)
            count += 2
        else:
            letter_tracker.update({letter: 1})
    if len(letter_tracker) > 0:
        count += 1
    return count
