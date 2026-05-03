# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSmallest(self, root):
        if root is None:
            return None
        
        return self.findSmallest(root.left) if root.left else root.val
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                new_value = self.findSmallest(root.right)
                root.right = self.deleteNode(root.right, new_value)
                root.val = new_value
                return root
        
        return root