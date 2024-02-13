def isValid(self, s: str) -> bool:
    tracker = []
    parentheses = {")": "(", "}": "{", "]": "["}
    current = None
    for letter in s:
        if letter in parentheses.values():
            tracker.append(letter)
            current = letter
        elif letter in parentheses.keys():
            if current == parentheses[letter]:
                tracker.pop()
                if len(tracker) == 0:
                    current = None
                else: 
                    current = tracker[len(tracker) - 1]
            else:
                return False
    if len(tracker) == 0:
        return True
    else:
        return False

