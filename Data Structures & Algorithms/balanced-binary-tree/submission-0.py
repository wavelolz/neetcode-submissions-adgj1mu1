# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def findHeight(root):
            if root is None:
                return 0

            left_height = findHeight(root.left)
            right_height = findHeight(root.right)

            if left_height == "F" or right_height == "F":
                return "F"

            if abs(left_height-right_height)<=1:
                return max(left_height, right_height)+1
            else:
                return "F"

        res = findHeight(root)
        print(res)
        if res == "F":
            return False
        else:
            return True



        
        