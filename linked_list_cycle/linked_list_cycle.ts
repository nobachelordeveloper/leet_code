class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

const hasCycle = (head: ListNode | null): boolean => {
  if (!head) {
    return false;
  }
  let slow: ListNode | null = head;
  let fast: ListNode | null = head;
  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;
    if (slow === fast) {
      return true;
    }
  }
  return false;
};

var hasCycleUsingMap = function (head) {
  //previous one was way too brute, using less brute now
  if (!head) {
    return false;
  }
  let curr = head;
  let nodeMap = new Map();
  while (curr) {
    if (nodeMap.has(curr)) {
      return true;
    }
    nodeMap.set(curr, true);
    curr = curr.next;
  }
  return false;
};
