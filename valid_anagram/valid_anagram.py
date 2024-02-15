# My Solution
def isAnagram(self, s: str, t: str) -> bool:
    tracker = {}
    for letter in s:
        if letter in tracker:
            tracker[letter] += 1
        else:
            tracker[letter] = 1
    for letter in t:
        if letter in tracker:
            tracker[letter] -= 1
        else:
            return False
    if all(value == 0 for value in tracker.values()):
        return True
    else:   
        return False


# Optimal Solution
def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
