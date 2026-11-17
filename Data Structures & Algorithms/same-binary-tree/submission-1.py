# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_p = deque()
        q_q = deque()

        if not q and not p:
            return True
        elif q and not p or p and not q:
            return False

        q_p.append(p)
        q_q.append(q)
        print(q_p, q_q)
        while q_p and q_q:
            for i in range(len(q_p)):
                print(q_p, q_q)
                curr_p = q_p.popleft()
                curr_q = q_q.popleft()

                if curr_p.val != curr_q.val:
                    return False
                
                if curr_p.left and curr_q.left:
                    q_p.append(curr_p.left)
                    q_q.append(curr_q.left)
                elif curr_p.left is None and curr_q.left is None:
                    pass
                else:
                    return False
                if curr_p.right and curr_q.right:
                    q_p.append(curr_p.right)
                    q_q.append(curr_q.right)
                elif curr_p.right is None and curr_q.right is None:
                    continue
                else:
                    return False
        return True
                
