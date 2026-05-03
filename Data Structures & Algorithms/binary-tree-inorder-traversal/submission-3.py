# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret_val = list()
        stack = []

        while root:
            if not root.left:
                ret_val.append(root.val)
                
                if root.right:
                    root = root.right
                elif stack:
                    root = stack.pop()
                    ret_val.append(root.val)
                    while not root.right and stack:
                        root = stack.pop()
                        ret_val.append(root.val)
                    
                    root = root.right
                else:
                    break
            else:
                stack.append(root)
                root = root.left
        
        return ret_val
