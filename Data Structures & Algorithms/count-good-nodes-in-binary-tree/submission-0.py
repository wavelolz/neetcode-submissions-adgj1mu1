from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for every level we need only the maximum value along this path so far
        
        queue = deque()
        queue.append([root, root.val])
        cnt = 1

        while queue:
            root, max_val = queue.popleft()
            if root.left:
                if root.left.val >= max_val:
                    queue.append([root.left, root.left.val])
                    print(f"root: {root.val}, root.left: {root.left.val}")
                    cnt += 1
                else:
                    queue.append([root.left, max_val])

            if root.right:
                if root.right.val >= max_val:
                    queue.append([root.right, root.right.val])
                    print(f"root: {root.val}, root.right: {root.right.val}")
                    cnt += 1
                else:
                    queue.append([root.right, max_val])
        return cnt
            
