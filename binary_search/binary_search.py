from typing import List
import math


# My Answer
def search(self, nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    halvingCount = math.ceil(len(nums) / 2)
    index = halvingCount - 1
    while halvingCount != 1:
        if nums[index] == target:
            return index
        else:
            halvingCount = math.ceil(halvingCount / 2)
            if nums[index] > target:
                index -= halvingCount
            else:
                if index + halvingCount >= len(nums):
                    index = len(nums) - 1
                else:
                    index += halvingCount
    if nums[index] == target:
        return index
    else:
        if nums[index] > target:
            index -= 1  
            if nums[index] == target:
                return index
        if nums[index] < target and index + 1 < len(nums):
            index += 1
            if nums[index] == target:
                return index
    return -1

# Optimal Answer
def search(self, nums: List[int], target: int) -> int:
    # left points at 0, right points at the last (n-1)
    # mid = (l + r)//2  (Lower) or l + (r-l) // 2
    # l <= r
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # num < target, move to the right half of the sub-array
        if nums[mid] < target:
            left = mid + 1 # you have to check until left is greater than right that would hit at the condition for while loop
        # num > target, move to the left half of the sub-array
        elif nums[mid] > target:
            right = mid - 1 # you have to check until right is less than left
        else:
            return mid
    return -1
