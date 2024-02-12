import test from "./test.json" with {type: "json"};

const isPermutation = (str1: String, str2: String) => {
  let isPassing = true;
  let letterCount = {};
  str1.split("").forEach((letter) => {
    if(letter in letterCount) {
      letterCount[letter] += 1;
    } else {
      letterCount[letter] = 1;
    }
  })
  str2.split("").forEach((letter) => {
    if(letter in letterCount) {
      letterCount[letter] -= 1;
    } else {
      isPassing = false;
    }
  })
  if(Object.values(letterCount).some(num => num !== 0)) {
    isPassing = false;
  }
  return isPassing;
}

test.forEach(input => {
  console.log(isPermutation(input["string1"], input["string2"]) === input["output"])
})
