# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)

        ret_val = []

        while q:
            curr = q.popleft()
            
            if not curr:
                ret_val.append(" ")
            else:
                ret_val.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)

        return "#".join(ret_val)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = deque(data.split("#"))
        curr_nodes = []
        root_node = None
        while values:
            if not curr_nodes:
                curr_val = values.popleft()
                if curr_val == " ":
                    curr_nodes.append(None)
                else:
                    root_node = TreeNode(curr_val)
                    curr_nodes.append(root_node)
            else:
                new_curr_nodes = []
                for curr_node in curr_nodes:
                    if curr_node is None:
                        continue
                    curr_val_left = values.popleft()
                    curr_val_right = values.popleft()

                    if curr_val_left == " ":
                        pass
                    else:
                        curr_node.left = TreeNode(curr_val_left)
                        new_curr_nodes.append(curr_node.left)
                    
                    if curr_val_right == " ":
                        continue
                    else:
                        curr_node.right = TreeNode(curr_val_right)
                        new_curr_nodes.append(curr_node.right)
                curr_nodes = new_curr_nodes
        
        return root_node

                    


            


















