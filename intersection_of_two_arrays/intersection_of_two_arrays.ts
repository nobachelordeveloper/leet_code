function intersection(nums1: number[], nums2: number[]): number[] {
  nums1.sort((a, b) => a - b);
  nums2.sort((a, b) => a - b);
  let leftIndex = 0;
  let rightIndex = 0;
  let intersection: number[] = [];
  while (leftIndex < nums1.length && rightIndex < nums2.length) {
    if (nums1[leftIndex] === nums2[rightIndex]) {
      if (intersection.length === 0) {
        intersection.push(nums1[leftIndex]);
      }
      if (intersection[intersection.length - 1] !== nums1[leftIndex]) {
        intersection.push(nums1[leftIndex]);
      }
      rightIndex += 1;
      leftIndex += 1;
    } else if (nums1[leftIndex] > nums2[rightIndex]) {
      rightIndex += 1;
    } else {
      leftIndex += 1;
    }
  }
  return intersection;
}

//Using Reduce
function intersectionUsingReduce(nums1: number[], nums2: number[]): number[] {
  const nums1Set = new Set(nums1);

  return nums2.reduce((acc: number[], cur: number) => {
    if (nums1Set.has(cur)) {
      acc.push(cur);
      nums1Set.delete(cur);
    }
    return acc;
  }, []);
}

//Using Set()
function intersectionUsingSet(nums1: number[], nums2: number[]): number[] {
  const set1 = new Set(nums1);
  const set2 = new Set(nums2);

  let res = new Set<number>();

  set1.forEach((item) => {
    if (set2.has(item)) {
      res.add(item);
    }
  });
  return Array.from(res);
}
