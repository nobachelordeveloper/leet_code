package remove_duplicates_from_sorted_array;

class Solution {
	public int removeDuplicates(int[] nums) {
		int placeholder = 1;
		for (int i = 1; i < nums.length; i++) {
			if (nums[i - 1] != nums[i]) {
				nums[placeholder] = nums[i];
				placeholder += 1;
			}
		}
		return placeholder;
	}
}