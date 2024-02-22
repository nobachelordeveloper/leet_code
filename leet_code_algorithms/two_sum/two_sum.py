from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
	checkedNumbers = []
	pairIndices = []
	for num in range(len(nums)):
		diff = target - nums[num]
		if diff in checkedNumbers:
			pairIndices = [checkedNumbers.index(diff), num]
		else:
			checkedNumbers.append(nums[num])
	return pairIndices
	