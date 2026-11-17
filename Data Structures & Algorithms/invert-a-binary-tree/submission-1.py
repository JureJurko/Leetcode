# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        q = deque()
        q.append(root)
        
        while q:
            curr = q.popleft()

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right) 
        
        return root
