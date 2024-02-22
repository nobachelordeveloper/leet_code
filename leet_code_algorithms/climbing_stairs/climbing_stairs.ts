const climbStairs = (n: number): number => {
  let left = 1;
  let right = 1;
  let start = 0;
  while (start < n - 1) {
    const temp = left;
    left = left + right;
    right = temp;
    start++;
  }
  return left;
};
