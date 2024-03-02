package practice;

class UsingLeftAndRightPointers {
    public int[] twoSum(int[] nums, int target) {
        int leftPointer = 0;
        int rightPointer = nums.length - 1;
        for (int i = 0; i < nums.length / 2; i++) {
            if (nums[leftPointer] + nums[rightPointer] == target) {
                return new int[] { leftPointer, rightPointer };
            } else {
                for (int j = i + 1; j < rightPointer; j++) {
                    if (nums[leftPointer] + nums[j] == target) {
                        return new int[] { leftPointer, j };
                    } else {
                        if (nums[rightPointer] + nums[j] == target) {
                            return new int[] { j, rightPointer };
                        }
                    }
                }
            }
            leftPointer++;
            rightPointer--;

        }
        return new int[] { 0, 0 };
    }
}