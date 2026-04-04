# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1s = " "
        l2s = " "

        while l1:
            l1s += str(l1.val)
            l1 = l1.next

        while l2:
            l2s += str(l2.val)
            l2 = l2.next

        l1i = int(l1s[::-1])
        l2i = int(l2s[::-1])
        s = str(l1i + l2i)[::-1]
        h = ListNode(val=int(s[0]))
        t = h
        for i in range(1, len(s)):
            t.next = ListNode(val=int(s[i]))
            t = t.next


        return h
        