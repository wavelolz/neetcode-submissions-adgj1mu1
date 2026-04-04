from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # there should be at least one node visible for every level
        # level order
        # use stack 

        result = []
        stack = deque([root])
        
        if not root:
            return []
            
        while stack:
            root = stack[-1]
            result.append(root.val)

            for _ in range(len(stack)):
                cur_node = stack.popleft()

                if cur_node.left:
                    stack.append(cur_node.left)

                if cur_node.right:
                    stack.append(cur_node.right)
            # for i in range(len(stack)):
            #     print(stack[i].val)
            # print("======")
        return result


        