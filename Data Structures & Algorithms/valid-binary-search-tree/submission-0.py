from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # each iteration check if left and right child are valid
        # each child should be fit between a boundry that starts with [-inf, inf] from root node
        # for right child update the lower bound with parent node value, left child update the upper bound



        def check(root, lower, upper):
            if not root:
                return True

            if not (lower < root.val < upper):
                return False

            return check(root.left, lower, root.val) and check(root.right, root.val, upper)

        return check(root, float("-inf"), float("inf"))


            





        

        

        