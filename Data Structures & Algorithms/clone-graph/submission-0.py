import collections
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m = {}
        if node is None:
            return None
        start = Node(val=node.val, neighbors=None)
        queue = collections.deque()
        queue.append((node, start))
        m[node] = start

        while queue:
            cur_original, cur_copy = queue.popleft()
            cur_neighbor = cur_original.neighbors
            for i in range(len(cur_neighbor)):
                if cur_neighbor[i] in m:
                    cur_copy.neighbors.append(m[cur_neighbor[i]])
                else:
                    original = cur_neighbor[i]
                    new = Node(val=original.val, neighbors=None)
                    cur_copy.neighbors.append(new)
                    queue.append((original, new))
                    m[original] = new 
        return start
        

                
                
            




        
        