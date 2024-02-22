from typing import List


# My Answer
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    leftIndex = 0
    rightIndex = 0
    intersection = []
    while leftIndex < len(nums1) and rightIndex < len(nums2):
        if nums1[leftIndex] == nums2[rightIndex]:
            if len(intersection) == 0:
                intersection.append(nums1[leftIndex])
            elif not intersection[len(intersection) - 1] == nums1[leftIndex]:
                intersection.append(nums1[leftIndex])
            else:
                pass
            rightIndex += 1
            leftIndex += 1
        elif nums1[leftIndex] > nums2[rightIndex]:
            rightIndex += 1
        else:
            leftIndex += 1
    return intersection
