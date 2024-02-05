package contains_duplicate;

import java.util.ArrayList;
import java.util.Arrays;

class MyAnswer {
	public boolean containsDuplicate(int[] nums) {
		var seenNumbers = new ArrayList<Integer>();
		for (int num : nums) {
			if (seenNumbers.contains(num)) {
				return true;
			} else {
				seenNumbers.add(num);
			}
		}
		return false;
	}
}

class UsingSort {
	public boolean containsDuplicate(int[] nums) {
		Arrays.sort(nums);
		for(int i = 0; i < nums.length; i++) {
			if(nums[i] == nums[i+1]) {
				return true;
			}
		}
		return false;
	}
}  