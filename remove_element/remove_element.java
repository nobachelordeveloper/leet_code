package remove_element;

class Solution {
	public int removeElement(int[] nums, int val) {
		int count = 0;
		for(int i = 0; i < nums.length; i++) {
			if(nums[i] != val) {
				nums[count] = nums[i];
				count++;
			}
		}
		return count;
	}

	public int removeElementTwo(int[] nums, int val) {
		int count = 0;
		for(final int num : nums) {
			if(num != val) {
				nums[count++] = num;
			}
		}
		return count;
	} 
}