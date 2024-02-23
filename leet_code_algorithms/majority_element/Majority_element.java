package majority_element;

import java.util.Arrays;

public class Majority_element {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[Math.floorDiv(nums.length, 2)];
    }
}
