class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

const mergeTwoLists = (
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null => {
  if (!list2) {
    return list1;
  }
  if (!list1) {
    return list2;
  }
  let dummy = new ListNode(-1);
  let current = dummy;
  while (list1 && list2) {
    if (list1.val > list2.val) {
      current.next = list2;
      list2 = list2.next;
    } else {
      current.next = list1;
      list1 = list1.next;
    }
    current = current.next;
  }
  if (!list2 && list1) {
    current.next = list1;
  }
  if (!list1 && list2) {
    current.next = list2;
  }
  return dummy.next;
};
