# My Answer
def containsDuplicate(self, nums: List[int]) -> bool:
    mySet = set(nums)
    if len(mySet) == len(nums):
        return False
    else:
        return True


# Using Counter
from collections import Counter


def containsDuplicate(self, nums: List[int]) -> bool:
    for k, v in Counter(nums).items():
        if v > 1:
            return True
    return False
