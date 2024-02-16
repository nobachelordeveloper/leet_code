// prettier-ignore
import test from "./test.json" with {type: "json"};

const one_away = (first, second) => {
  const shorter_string = first.length >= second.length ? second : first;
  const longer_string = first.length >= second.length ? first : second;
  let is_one_away = true;
  if (longer_string.length - shorter_string.length > 1) {
    return false;
  }
  let index_shorter = 0;
  let index_longer = 0;
  let difference_found = false;

  while (index_shorter < shorter_string.length) {
    if (shorter_string[index_shorter] !== longer_string[index_longer]) {
      if (difference_found) {
        is_one_away = false;
        break;
      } else {
        difference_found = true;
      }
      if (shorter_string.length !== longer_string.length) {
        index_longer++;
      } else {
        index_longer++;
        index_shorter++;
      }
    } else {
      index_longer++;
      index_shorter++;
    }
  }
  return is_one_away;
};

//#1
const solution = one_away;
if (true) {
  let errors = 0;
  let error_indices = [];
  test.forEach((inputLine) => {
    const input = inputLine["input"];
    //#2
    const output = solution(input["first"], input["second"]);
    if (!output === inputLine["output"]) {
      console.log(`There is an error at #${inputLine["index"]}`);
      console.log(`My answer was: ${output}`);
      console.log(`Given ans was: ${inputLine["output"]} `);
      errors++;
      error_indices.push(inputLine["index"]);
    }
  });
  if (errors) {
    console.log(`There were ${errors} errors`);
    error_indices.forEach((error) => {
      console.log(`Please check #${error}`);
    });
  } else {
    console.log("No errors were found");
  }
} else {
  //#3
  const index = 13;
  const inputLine = test.find((inputLine) => inputLine.index === index);
  const input = inputLine["input"];
  Object.keys(input).forEach((key) => {
    console.log(`The argument for "${key}" is:           ${input[key]}`);
  });
  //#4
  const outcome = solution(input["first"], input["second"]);
  console.log("END:", outcome);
}
