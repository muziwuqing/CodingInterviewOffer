class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reversePrint(head):
    lst = []
    tmp = head 
    while tmp != None:
        lst.append(tmp.val)
        tmp = tmp.next
    n = len(lst)
    for i in range(n//2+1):
        lst[i], lst[n-i-1] = lst[n-i-1], lst[i]
    return lst
    


def printListNode(head):
    nums = []
    while head != None:
        nums.append(head.val)
        head = head.next
    print(nums)

head = ListNode(0)
tail = head
for i in range(1, 10):
    node = ListNode(i)
    tail.next = node
    tail = tail.next

printListNode(head)
res = reversePrint(head)
print(res)
