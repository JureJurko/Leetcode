# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret_val = []
        
        def dfs(node, depth):
            if not node:
                return None
            
            if depth >= len(ret_val):
                ret_val.append(node.val)
            else:
                ret_val[depth] = node.val
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return ret_val


