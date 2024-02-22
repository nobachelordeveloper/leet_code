// My Solution

var isPalindrome = (s:string) => {
  const lowCaseString = s.toLowerCase();
  let formattedS = "";
  let reversedS = "";
  for (let i = 0; i < lowCaseString.length; i++) {
    if (lowCaseString[i].match(/[0123456789a-z]/)) {
      formattedS += lowCaseString[i];
    }
  }
  for (let x = formattedS.length - 1; x > -1; x--) {
    reversedS += formattedS[x];
  }
  return formattedS === reversedS;
};

// ChatGPT Solution
var isPalindrome = function (s:string) {
  s = s.replace(/[\W_]/g, "").toLowerCase();

  let left = 0;
  let right = s.length - 1;

  while (right >= left) {
    if (s[left] !== s[right]) {
      return false;
    }

    right--;
    left++;
  }

  return true;
};
