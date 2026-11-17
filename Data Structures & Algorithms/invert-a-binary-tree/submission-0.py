# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        if not root:
            return root
        q.append(root)
        while q:
            curr = q.popleft()

            if curr.left is not None and curr.right is not None:
                q.append(curr.left)
                q.append(curr.right)

                tmp = curr.left
                curr.left = curr.right
                curr.right = tmp
            elif curr.left is not None:
                q.append(curr.left)

                curr.right = curr.left
                curr.left = None
            elif curr.right is not None:
                q.append(curr.right)
                curr.left = curr.right
                curr.right = None
        
        return root
