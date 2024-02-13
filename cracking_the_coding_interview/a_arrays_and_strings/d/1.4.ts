import test from "./test.json" with {type: "json"};

const is_palindrome_permutation = (s: string): boolean => {
  const letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"];
  let tracker = {};
  for(let i = 0; i < s.length; i++) {
    const lowerLetter = s[i].toLowerCase();
    if(letters.includes(lowerLetter)) {
      if(Object.keys(tracker).includes(lowerLetter)) {
        delete tracker[lowerLetter];
      } else {
        tracker[lowerLetter] = 1;
      }
    }
  }
  return Object.keys(tracker).length <= 1;
}

test.forEach(input => {
  console.log(`#${input["index"]}: ${is_palindrome_permutation(input["input"]["s"]) === input["output"]}`)
})
