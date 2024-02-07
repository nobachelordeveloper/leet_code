// My Answer
function reverseWords(s: string): string {
  const wordList = s.trim().split(/\s+/);
  const reversedWordList = wordList.reverse();
  return reversedWordList.join(" ");
}

//run "tsc .\reverse_words_in_a_string.ts"
//and generate reverse_words_in_a_string.js file in the same directory to debug
