# MY BRUTE FORCE SOLUTION
def hasCycle(self, head: Optional[ListNode]) -> bool:
    history = []
    index = 0
    if not head:
        return False

    def seen(node, history):
        if node in history:
            return history.index(node)
        else:
            if node.next == None:
                return -1
            else:
                new_history = history + [node]
                return self.seen(node.next, new_history)

    return seen(head, history) >= 0

# OPTIMAL SOLUTION
def hasCycleOptimal(self, head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
