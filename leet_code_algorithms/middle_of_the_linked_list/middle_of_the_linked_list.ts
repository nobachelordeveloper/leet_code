class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

const middleNode = (head: ListNode): ListNode | null => {
  let fast: ListNode | null = head;
  let slow: ListNode | null = head;
  while (fast && fast.next) {
    slow = slow ? slow.next : null;
    fast = fast.next.next;
  }
  return slow;
};
