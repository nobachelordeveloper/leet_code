function pivotIndex(nums: number[]): number {
  let totalSum: number = 0;
  nums.forEach((num) => {
    totalSum += num;
  });
  let startingSum: number = 0;
  let index: number = 0;
  while (index < nums.length) {
    if (totalSum - nums[index] - startingSum == startingSum) {
      return index;
    }
    startingSum += nums[index];
    index += 1;
  }
  return -1;
}
