/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  let placeholder = 1;
	nums.forEach((num, i) => {
		if(i === 0) {
			biggestNumber = num;
		} else {
			if(num !== biggestNumber) {
				nums[placeholder] = num;
				biggestNumber = num;
				placeholder += 1;
			}
		}
	return placeholder;
	})
};