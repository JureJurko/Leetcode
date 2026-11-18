# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        good_nodes = 1
        q = deque([(root, root.val)])

        while q:
            for i in range(len(q)):
                node, curr_max_val = q.popleft()

                if node.left:
                    if curr_max_val <= node.left.val:
                        good_nodes += 1
                    q.append((node.left, max(node.left.val, curr_max_val)))
                if node.right:
                    if curr_max_val <= node.right.val:
                        good_nodes += 1
                    q.append((node.right, max(node.right.val, curr_max_val)))
        
        return good_nodes