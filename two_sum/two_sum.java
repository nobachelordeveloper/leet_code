import java.util.ArrayList;

class MyAnswer {
	public int[] twoSum(int[] nums, int target) {
		var checkedNumbers = new ArrayList<Integer>();
		int[] pairIndices = new int[2];
		for (int i = 0; i < nums.length; i++) {
			var diff = target - nums[i];
			if (checkedNumbers.contains(diff)) {
				pairIndices[0] = checkedNumbers.indexOf(diff);
				pairIndices[1] = i;
			} else {
				checkedNumbers.add(nums[i]);
			}
		}
		return pairIndices;
	}
}

class UsingLeftAndRightPointers {
	public int[] twoSum(int[] nums, int target) {
		int leftPointer = 0;
		int rightPointer = nums.length - 1;
		for (int i = 0; i < nums.length / 2; i++) {
			if (nums[leftPointer] + nums[rightPointer] == target) {
				return new int[] { leftPointer, rightPointer };
			}
			for (int j = i + 1; j < rightPointer; j++) {
				if (nums[leftPointer] + nums[j] == target) {
					return new int[] { leftPointer, j };
				}
				if (nums[j] + nums[rightPointer] == target) {
					return new int[] { j, rightPointer };
				}
			}
			leftPointer++;
			rightPointer--;
		}
		return new int[] { 0, 0 };
	}
}