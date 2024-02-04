/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
	let count = 0;
	nums.forEach((num) => {
		if(num !== val) {
			nums[count++] = num;
		}
	})
	return count;
};