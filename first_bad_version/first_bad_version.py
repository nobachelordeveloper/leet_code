# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Maximum number of elements in a python list is 536,870,912


# My Solution
def firstBadVersion(self, n: int) -> int:
    left = 1
    right = n
    if n == 1:
        return 1
    while left <= right:
        mid = left + (right - left) // 2  # avoid integer overflow
        if isBadVersion(mid) == False:
            left = mid + 1
        else:
            if BadVersion(mid - 1) == False:
                return mid - 1
            else:
                right = mid - 1


# Optimal Solution
def firstBadVersion(self, n: int) -> int:
    left = 1
    while left < n:
        mid = (left + n) // 2
        if isBadVersion(mid):
            n = mid
        else:
            left = mid + 1

    return left
    # return n  --> this works too

# the above keeps running until left is one less than n. n will be set to where isBadVersion returns true and left will continue updating until it is one less than n. the last left = mid + 1 that exits the while loop jumps from the good version to the first bad version