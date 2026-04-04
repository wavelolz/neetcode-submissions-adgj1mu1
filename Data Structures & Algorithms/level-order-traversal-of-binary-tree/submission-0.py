from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            current_level_nodes = []
            for _ in range(len(queue)):
                root = queue.popleft()
                current_level_nodes.append(root.val)

                if root.left:
                    queue.append(root.left)

                if root.right:
                    queue.append(root.right)
            result.append(current_level_nodes)
        return result







