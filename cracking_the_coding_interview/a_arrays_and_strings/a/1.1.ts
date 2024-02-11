export {}

// Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

const string_one = "hello";
const string_two = "world";
const string_three = "apple";
const string_four = "12345";
const string_five = "abracadabra";

const isUniqueCharacters = (str: string) => {
  let hash_table = {};
  let isUnique = true;

  str.split("").forEach((letter) => {
    if (Object.keys(hash_table).includes(letter)) {
      isUnique = false;
    } else {
      hash_table[letter] = 1;
    }
  })
  return isUnique;
}

//Optimal Answer
const isUniqueCharactersOptimal = (str: string) => {
  let hash_table = {};
  for (let letter of str) {
    if (hash_table[letter]) {
      return false; // If duplicate character found, return false
    } else {
      hash_table[letter] = true;
    }
  }
  return true; // If no duplicate characters found, return true
};
