package maximum_subarray;

public class Maximum_subarray {
    public int maxSubArray(int[] nums) {
        int current_sum = 0;
        int overall_max = nums[0];
        for (var i = 0; i < nums.length; i++) {
            current_sum += nums[i];
            overall_max = Math.max(current_sum, overall_max);
            if (current_sum < 0) {
                current_sum = 0;
            }
        }
        return overall_max;
    }
}
