# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head

        while s:
            f = f.next
            if not s.next:
                return False
            elif not s.next.next:
                return False
            else:
                s = s.next.next
            if f == s:
                return True
        return False


        