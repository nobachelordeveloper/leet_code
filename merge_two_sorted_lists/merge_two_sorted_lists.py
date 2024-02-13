# My Solution
def mergeTwoLists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if list1 == None:
        return list2
    if list2 == None:
        return list1
    if list1.val > list2.val:
        head = list2
        list2 = list2.next      
    else:
        head = list1
        list1 = list1.next
    current = head
    while list1 != None and list2 != None:
        if list1.val > list2.val:
            current.next = list2
            list2 = list2.next
        else:
            current.next = list1
            list1 = list1.next
        current = current.next
    if list1 == None and list2 != None:
        current.next = list2
    if list2 == None and list1 != None:
        current.next = list1
    return head


# ChatGPT Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode(-1)  # Dummy head for ease of handling edge cases
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the non-null list if one remains
    current.next = list1 if list1 else list2

    return dummy.next  # Return the merged list starting from dummy.next
