// Write a method to replace all spaces in a strin with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

// EXAMPLE
// Input: "Mr John Smith     ", 13
// Output: "Mr%20John%20Smith"

import test from "./test.json" with {type: "json"};

const URLify = (s:string, true_length:number) => {
  let result =  "";
  for (let i = 0; i < true_length; i++) {
    if(i > (s.length-1)) {
      result += "%20";

    } else if (s[i] === " ") {
      result += "%20";
    } else {
      result += s[i];
    }
  }
  return result;
}

test.forEach(input => {
  console.log(`#${input["index"]}: ${URLify(input["input"]["string"], input["input"]["true_length"]) === input["output"]}`)
})
