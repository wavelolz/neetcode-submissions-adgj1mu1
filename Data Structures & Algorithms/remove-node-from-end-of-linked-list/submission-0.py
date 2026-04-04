# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        else:
            l = []
            tmp = head

            while tmp:
                l.append(tmp)
                tmp = tmp.next
            N = len(l)
            if n == N:
                return head.next
            elif n == 1:
                l[-2].next = None
                return head
            else:
                l[N-n-1].next = l[N-n+1]
                return head
        