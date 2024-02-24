def addBinary(self, a: str, b: str) -> str:
    sum = ""
    carry = 0
    reverseA, reverseB = a[::-1], b[::-1]
    for index in range(max(len(a), len(b))):
        int_a = ord(reverseA[index]) - ord("0") if index < len(a) else 0
        int_b = ord(reverseB[index]) - ord("0") if index < len(b) else 0
        total = int_a + int_b + carry
        sum = str(total % 2) + sum
        carry = total//2
    if carry:
        sum = "1" + sum
    return sum
