using System.Linq;

namespace leet_code_algorithms
{
    public class Two_sum
    {
        public static int[] TwoSum(int[] nums, int target)
        {
            var checkedNumbers = new List<int>();
            int[] pairIndices = new int[2];
            for (int i = 0; i < nums.Length; i++)
            {
                var diff = target - nums[i];
                if (checkedNumbers.Contains(diff))
                {
                    pairIndices[0] = checkedNumbers.IndexOf(diff);
                    pairIndices[1] = i;
                }
                else
                {
                    checkedNumbers.Add(nums[i]);
                }
            }
            return pairIndices;
        }
    }
}
