# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i1 = list1
        i2 = list2
        sol = []

        while i1 and i2:
            if i1.val <= i2.val:
                sol.append(i1)
                i1 = i1.next
            else:
                sol.append(i2)
                i2 = i2.next

        if i1 is None:
            while i2:
                sol.append(i2)
                i2 = i2.next
        
        if i2 is None:
            while i1:
                sol.append(i1)
                i1 = i1.next
        
        for i in sol:
            print(i.val)
        for i in range(len(sol)-1):
            cur = sol[i]
            cur.next = sol[i+1]
            cur = cur.next

        return sol[0] if len(sol)>0 else None



        