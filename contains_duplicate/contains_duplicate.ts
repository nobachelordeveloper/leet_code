// My Answer
function containsDuplicate(nums: number[]): boolean {
  nums.sort();
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == nums[i + 1]) {
      return true;
    }
  }
  return false;
}

// Using Set
function containsDuplicateTwo(nums: number[]): boolean {
  const set = new Set();
  for (const num of nums) {
    if (set.has(num)) {
      return true;
    }
    set.add(num);
  }
  return false;
}

function containsDuplicateThree(nums: number[]): boolean {
  return Array.from(new Set(nums)).length != nums.length;
}

//using Map
function containsDuplicateMap(nums: number[]): boolean {
  const numCount = new Map<number, number>();
  for (const num of nums) {
    if (numCount.has(num)) {
      return true;
    }
    numCount.set(num, 1);
  }
  return false;
}
