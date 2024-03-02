/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/*My Answer*/
var twoSum = function (nums, target) {
  let seen = [];
  let indices = [];
  nums.forEach((num, i) => {
    if(seen.includes(target-num)) {
      indices = [i, seen.indexOf(target-num)]
    } else {
      seen.push(num)
    }
  })
  return indices;
}

var twoSum = function (nums, target) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i];
    if(map.has(complement)) {
      return [map.get(complement), i];
    } else {
      map.set(nums[i], i);
    }
  }
  return []
}