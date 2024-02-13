const isValid = (s: String) => {
  let tracker: String[] = [];
  const parentheses = { ")": "(", "}": "{", "]": "[" };
  let current: String = "";
  for (let i = 0; i < s.length; i++) {
    if (Object.values(parentheses).includes(s[i])) {
      tracker.push(s[i]);
      current = s[i];
    } else if (Object.keys(parentheses).includes(s[i])) {
      if (current === parentheses[s[i]]) {
        tracker.pop();
        if (tracker.length === 0) {
          current = "";
        } else {
          current = tracker[tracker.length - 1];
        }
      } else {
        return false;
      }
    }
  }
  if (tracker.length === 0) {
    return true;
  } else {
    return false;
  }
};
