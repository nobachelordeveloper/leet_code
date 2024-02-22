package find_pivot_index;

public class Find_pivot_index {
    public int pivotIndex(int[] nums) {
        var totalSum = 0;
        for (int i = 0; i < nums.length; i++) {
            totalSum += nums[i];
        }
        var startingSum = 0;
        var index = 0;
        while (index < nums.length) {
            if (totalSum - nums[index] - startingSum == startingSum) {
                return index;
            }
            startingSum += nums[index];
            index += 1;
        }
        return -1;
    }
}
