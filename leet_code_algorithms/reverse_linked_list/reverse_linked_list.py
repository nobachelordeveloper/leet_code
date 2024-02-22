class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseListIteratively(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while (head):
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def reverseListRecursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    def reverseList(curr, prev):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        if curr:
            return reverseList(curr, prev)
        else:
            return prev
    if head:
        prev = reverseList(head, prev)
    else:
        prev = None
    return prev
