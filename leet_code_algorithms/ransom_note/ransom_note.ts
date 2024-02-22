const canConstruct = (ransomNote: string, magazine: string) => {
  let isPossible = true;
  for (const letter of ransomNote) {
    if (magazine.indexOf(letter) >= 0 && isPossible) {
      magazine = magazine.replace(letter, "");
    } else {
      isPossible = false;
    }
  }
  return isPossible;
};
