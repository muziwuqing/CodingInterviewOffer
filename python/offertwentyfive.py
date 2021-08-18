class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None and l2 == None:
        return None
    if l1 == None and l2 != None:
        return l2
    if l2 == None and l1 != None:
        return l1
    head = r = ListNode(0)
    p1, p2 = l1, l2
    while p1 and p2:
        if p1.val <= p2.val:
            tmp = ListNode(p1.val)
            p1 = p1.next
            r.next = tmp
            r = r.next
        else:
            tmp = ListNode(p2.val)
            p2 = p2.next
            r.next = tmp
            r = r.next
    if p1:
        r.next = p1
    if p2:
        r.next = p2
    return head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
mergeTwoLists(l1, l2)