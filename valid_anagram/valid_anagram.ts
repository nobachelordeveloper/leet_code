// My Solution
const isAnagram = (s: string, t: string) => {
  let tracker = {};
  let passing = true;
  for (let char of s) {
    if (char in tracker) {
      //if(Object.keys(tracker).includes(char)) is obsolete
      tracker[char] += 1;
    } else {
      tracker[char] = 1;
    }
  }
  for (let char of t) {
    if (char in tracker) {
      tracker[char] -= 1;
    } else {
      passing = false;
    }
  }
  if (!Object.values(tracker).every((value) => value === 0)) {
    passing = false;
  }
  return passing;
};

//Optimal Solution
var isAnagramOptimal = function (s, t) {
  if (s.length != t.length) return false;

  const charMap = Array(26).fill(0);

  for (let i = 0; i < s.length; i++) {
    charMap[s.charCodeAt(i) - "a".charCodeAt(0)]++;
    charMap[t.charCodeAt(i) - "a".charCodeAt(0)]--;
  }

  return charMap.every((count) => count === 0);
};

//Using Maps
var isAnagramUsingMap = function (s, t) {
  if (s.length != t.length) return false;

  const charMap = Array(26).fill(0);

  for (let i = 0; i < s.length; i++) {
    charMap[s.charCodeAt(i) - "a".charCodeAt(0)]++;
    charMap[t.charCodeAt(i) - "a".charCodeAt(0)]--;
  }

  return charMap.every((count) => count === 0);
};
