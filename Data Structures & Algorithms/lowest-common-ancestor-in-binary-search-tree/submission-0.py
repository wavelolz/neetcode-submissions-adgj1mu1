# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p < node and q > node or p > node and q < node, it means the current node is LCA
        # if p < node and q < node then LCA is in the left subtree
        # if p > node and q > node then LCA is in the right subtree

        if p.val > q.val:
            p, q = q, p

        def searchLCA(root):
            if (p.val < root.val and q.val > root.val) or (p.val == root.val) or (q.val == root.val):
                return root

            if p.val < root.val and q.val < root.val:
                root = searchLCA(root.left)
            elif p.val > root.val and q.val > root.val:
                root = searchLCA(root.right)

            return root
        lca = searchLCA(root)
        return lca
        