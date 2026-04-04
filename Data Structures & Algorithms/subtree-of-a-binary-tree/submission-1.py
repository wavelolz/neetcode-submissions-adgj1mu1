# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def compare(subRoot, root):
            if not subRoot and not root:
                return True

            if not subRoot or not root or subRoot.val != root.val:
                return False

            return compare(subRoot.left, root.left) and compare(subRoot.right, root.right)
        
        return compare(subRoot, root) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        