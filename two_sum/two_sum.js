/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/*My Answer*/
var twoSum = function (nums, target) {
  let checkedNumbers = [];
  let pairIndices = [];
  nums.forEach((num, i) => {
    const diff = target - num;
    const index = checkedNumbers.indexOf(diff);
    if (index >= 0) {
      pairIndices = [index, i];
    } else {
      checkedNumbers.push(num);
    }
  });
  return pairIndices;
};

/*Using Map*/
var twoSum = function (nums, target) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i];
    if (map.has(complement)) {
      return [map.get(complement), i];
    } else {
      map.set(nums[i], i);
    }
  }
  return [];
};
