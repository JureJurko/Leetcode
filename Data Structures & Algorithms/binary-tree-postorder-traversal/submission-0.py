# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, result = [root], []

        while stack:
            curr = stack.pop()
            result.append(curr.val)

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return result[::-1]
        