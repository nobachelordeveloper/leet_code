const majorityElement = (nums: number[]): number => {
  nums.sort((a, b) => {
    return a - b;
  });
  return nums[Math.floor(nums.length / 2)];
};
