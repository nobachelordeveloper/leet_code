class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        overall_max = nums[0]
        for number in nums:
            current_sum += number
            overall_max = max(overall_max, current_sum)
            if current_sum < 0:
                current_sum = 0
        return overall_max
