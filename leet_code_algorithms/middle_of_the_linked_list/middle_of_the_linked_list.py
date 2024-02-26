class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# MY SOLUTION
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        node_list_length = 0
        if head.next == None:
            return head
        current = head
        while current:
            node_list.append(current)
            node_list_length += 1
            current = current.next
        return node_list[node_list_length//2]

# OPTIMAL SOLUTION
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s,f=head,head
        while (f and f.next):
            s=s.next
            f=f.next.next
        return s