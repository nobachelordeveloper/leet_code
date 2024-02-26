/**
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = (nums: number[]): number => {
  let current_sum = 0;
  let overall_max = nums[0];
  for (let index = 0; index < nums.length; index++) {
    current_sum += nums[index];
    overall_max = Math.max(overall_max, current_sum);
    if (current_sum < 0) {
      current_sum = 0;
    }
  }
  return overall_max;
};

//OPTIMAL ANSWER

var maxSubArrayOptimal = function (nums: number[]): number {
  let maxSum = nums[0];
  let res = nums[0];
  for (let i = 1; i < nums.length; i++) {
    maxSum = Math.max(maxSum + nums[i], nums[i]);
    res = Math.max(maxSum, res);
  }
  return res;
};
