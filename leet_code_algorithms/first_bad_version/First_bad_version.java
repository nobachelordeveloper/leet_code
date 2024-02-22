package first_bad_version;

public class First_bad_version {
    public int firstBadVersion(int n) {
        int left = 0;
        while (left < n) {
            int mid = left + Math.floorDiv(n - left, 2);
            if (isBadVersion(mid)) {
                n = mid;
            } else {
                left = mid + 1;
            }
        }
        return n;
    }

    private boolean isBadVersion(int mid) {
        throw new UnsupportedOperationException("Unimplemented method 'isBadVersion'");
    }
}
