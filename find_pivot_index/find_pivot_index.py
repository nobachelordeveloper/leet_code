def pivotIndex(self, nums: List[int]) -> int:
    totalSum = 0
    for num in nums:
        totalSum += num
    startingSum = 0
    index = 0
    while(index < len(numbers)):
        if(totalSum - numbers[index] - startingSum == startingSum):
            return index
        startingSum += numbers[index]
        index += 1
    return -1
