# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.cur_inx = 0

        in_order_map = {val: pos for pos, val in enumerate(inorder)}

        def arr_to_tree(left_inx, right_inx):
            if left_inx > right_inx:
                return None

            root_val = preorder[self.cur_inx]
            self.cur_inx += 1
            root = TreeNode(root_val)

            b = in_order_map[root_val]

            root.left = arr_to_tree(left_inx, b-1)
            root.right = arr_to_tree(b+1, right_inx)
            return root
        return arr_to_tree(0, len(preorder)-1)



        