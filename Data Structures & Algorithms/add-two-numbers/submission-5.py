class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1t = l1
        l2t = l2
        while l1t and l2t:
            s = l1t.val + l2t.val

            if s>9:
                l2t.val = s-10
                if l2t.next is None:
                    l2t.next = ListNode(val=1)
                else:
                    l2t.next.val += 1
            else:
                l2t.val = s

            if l1t.next is None and l2t.next is not None:
                l1t.next = ListNode(val=0)
            
            if l1t.next is not None and l2t.next is None:
                l2t.next = ListNode(val=0)
            l1t = l1t.next
            l2t = l2t.next

        return l2