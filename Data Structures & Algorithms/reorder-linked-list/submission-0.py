# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        tr = head
        while tr:
            l.append(tr)
            tr = tr.next

        low = 0 
        high = len(l)-1

        hd = ListNode()
        cur = hd

        while low<high:
            cur.next = l[low]
            cur = cur.next
            low += 1

            cur.next = l[high]
            cur = cur.next
            high -= 1

        if low==high:
            cur.next = l[low]
            cur = cur.next
        cur.next = None
        head = hd.next
        





        