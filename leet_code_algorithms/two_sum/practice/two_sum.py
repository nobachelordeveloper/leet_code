from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = [nums[0]]
    for num in range(1, len(nums)):
        diff = target - nums[num]
        if diff in seen:
            return [seen.index(diff), num]
        else:
            seen.append(nums[num])

print(twoSum("",[2,7,11,15],9))