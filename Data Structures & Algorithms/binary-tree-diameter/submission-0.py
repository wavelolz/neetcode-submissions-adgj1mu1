# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdia = 0

        def dfs(node):
            if node is None:
                return 0

            dleft = dfs(node.left)
            dright = dfs(node.right)

            if dleft+dright>self.maxdia:
                self.maxdia = dleft+dright

            return 1+max(dleft, dright)

        dfs(root)
        return self.maxdia
        