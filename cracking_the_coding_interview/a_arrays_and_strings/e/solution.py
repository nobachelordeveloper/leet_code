def solution(first, second):
    # Quick length check
    if abs(len(first) - len(second)) > 1:
        return False
    
    # Get the shorter and longer string
    s1 = first if len(first) < len(second) else second
    s2 = second if len(first) < len(second) else first
    
    index1 = 0
    index2 = 0
    found_difference = False
    
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            # More than one difference found
            if found_difference:
                return False
            found_difference = True
            
            # If lengths are different, increment longer string index
            if len(s1) != len(s2):
                index2 += 1
                continue
        index1 += 1
        index2 += 1

    return True

if __name__ == "__main__":
    # Test the function with examples
    print(solution("test", "best"))
