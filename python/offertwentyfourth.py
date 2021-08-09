class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    rhead = ListNode(None)
    head = head.next
    while head is not None:
        node = ListNode(head.val)
        node.next = rhead.next
        rhead.next = node
        head = head.next
    return rhead


def printList(head):
    head = head.next
    while head is not None:
        print(head.val)
        head = head.next


def constructList(arr):
    head = ListNode(None)
    tail = head
    for i in range(len(arr)):
        node = ListNode(arr[i])
        tail.next = node
        tail = tail.next
    return head


arr = [1, 2, 3, 4, 5, 6, 7]
ln = constructList(arr)
printList(ln)
res = reverseList(ln)
printList(res)
