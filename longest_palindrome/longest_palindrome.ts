//My Solution
const longestPalindrome = (s: string): number => {
  let letter_tracker = {};
  let count = 0;
  for (const letter of s) {
    if (Object.keys(letter_tracker).includes(letter)) {
      delete letter_tracker[letter];
      count += 2;
    } else {
      letter_tracker[letter] = 1;
    }
  }
  if (Object.keys(letter_tracker).length > 0) {
    count += 1;
  }
  return count;
};

//Optimal Solution using set()
var longestPalindromeUsingSet = function (s: string) {
  let set = new Set(),
    count = 0;
  for (let letter of s) {
    if (set.has(letter)) {
      count += 2;
      set.delete(letter);
    } else set.add(letter);
  }
  return count + (set.size > 0 ? 1 : 0);
};
