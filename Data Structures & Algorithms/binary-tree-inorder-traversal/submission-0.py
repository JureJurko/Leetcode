# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret_val = list()
        if not root:
            return []
        
        ret_val.extend(self.inorderTraversal(root.left))
        ret_val.append(root.val)
        ret_val.extend(self.inorderTraversal(root.right))

        return ret_val
