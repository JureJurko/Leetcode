# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ret_val = root
        if not root:
            return TreeNode(val)
        
        while True:
            if val > root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break
            elif val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break
            else:
                return TreeNode(val)

        return ret_val
