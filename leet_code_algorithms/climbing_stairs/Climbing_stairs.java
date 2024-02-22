package climbing_stairs;

public class Climbing_stairs {
    public int climbStairs(int n) {
        int left = 1;
        int right = 1;
        for (var i = 0; i < n - 1; i++) {
            int temp = left;
            left = left + right;
            right = temp;
        }
        return left;
    }
}
