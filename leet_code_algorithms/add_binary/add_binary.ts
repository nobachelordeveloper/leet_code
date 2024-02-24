const addBinary = (a: string, b: string): string => {
  let total = "";
  let carry = 0;
  const range = a.length > b.length ? a.length : b.length;
  for (let i = 0; i < range; i++) {
    const int_a = i < a.length ? parseInt(a[a.length - 1 - i]) : 0;
    const int_b = i < b.length ? parseInt(b[b.length - 1 - i]) : 0;
    const sum = int_a + int_b + carry;
    total = (sum % 2).toString() + total;
    carry = Math.floor(sum / 2);
  }
  if (carry) {
    total = "1" + total;
  }
  return total;
};
