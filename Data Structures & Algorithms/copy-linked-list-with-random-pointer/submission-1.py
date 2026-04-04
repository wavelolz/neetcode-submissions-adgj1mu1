"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}

        ch = head
        while ch:
            m[ch] = Node(ch.val, None, None)
            ch = ch.next

        ch = head

        while ch:
            if ch.next:
                m[ch].next = m[ch.next]
            if ch.random:
                m[ch].random = m[ch.random]
            ch = ch.next

        return None if len(m)==0 else m[head]

        

        