package intersection_of_two_arrays;

import java.util.ArrayList;
import java.util.Arrays;

public class Intersection_of_two_arrays {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        var leftIndex = 0;
        var rightIndex = 0;
        ArrayList<Integer> intersection = new ArrayList<>();

        while (leftIndex < nums1.length && rightIndex < nums2.length) {
            if (nums1[leftIndex] == nums2[rightIndex]) {
                if (intersection.size() == 0) {
                    intersection.add(nums1[leftIndex]);
                }
                if (intersection.get(intersection.size() - 1) != nums1[leftIndex]) {
                    intersection.add(nums1[leftIndex]);
                }
                rightIndex += 1;
                leftIndex += 1;
            } else if (nums1[leftIndex] > nums2[rightIndex]) {
                rightIndex += 1;
            } else {
                leftIndex += 1;
            }
        }
        int[] intersectionArray = new int[intersection.size()];
        for (int i = 0; i < intersectionArray.length; i++) {
            intersectionArray[i] = intersection.get(i).intValue();
        }
        return intersectionArray;
    }
}
