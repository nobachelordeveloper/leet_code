from typing import List

# My Answer
def removeDuplicates(self, nums: List[int]) -> int:
	biggestNumber = nums[0]
	indice = []
	for i in range(1, len(nums)):
		if(biggestNumber == nums[i]):
			indice,append(i)
		else:
			biggestNumber = nums[i]
		reverseIndice = indice[::-1]
		for index in reverseIndice:
			nums.pop(index)
		return len(nums)
# O(n^2) solution

# O(n) Solution
def removeDuplicates(self, nums):
	replace = 1
	for i in range(1, len(nums)):
		if nums[i-1] != nums[i]:
			nums[replace] = nums[i]
			replace += 1
	return replace

