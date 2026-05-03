class TreeNode:
    def __init__(self, key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return
        
        curr = self.root
        while True:
            if curr.key < key:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    break
            elif curr.key > key:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    break
            else:
                curr.val = new_node.val
                break
            
    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if curr.key > key:
                curr = curr.right
            elif curr.key < key:
                curr = curr.left
            else:
                return curr.val
        
        return -1

    def getMin(self) -> int:
        vals = []
        if not self.root:
            return -1
        
        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            vals.append(root.val)
            dfs(root.right)
        
        dfs(self.root)
        return vals[0]

    def getMax(self) -> int:
        vals = []
        if not self.root:
            return -1
        
        def dfs(root):
            if not root:
                return None
            
            dfs(root.right)
            vals.append(root.val)
            dfs(root.left)
        
        dfs(self.root)
        return vals[0]

    def remove(self, key: int) -> None:
        curr = self.root
        prev = curr

        while curr:
            if curr.key > key:
                prev = curr
                curr = curr.left
            elif curr.key < key:
                prev = curr
                curr = curr.right
            else:
                break

        if curr:
            if not curr.left and not curr.right:
                if prev.key == curr.key:
                    self.root = None  
                elif prev.left and prev.left.key == curr.key:
                    prev.left = None
                else:
                    prev.right = None
            elif not curr.right:
                new_curr = curr.left
                curr.val = new_curr.val
                curr.key = new_curr.key
                curr.right = new_curr.right
                curr.left = new_curr.left
            elif not curr.left:
                new_curr = curr.right
                curr.val = new_curr.val
                curr.key = new_curr.key
                curr.right = new_curr.right
                curr.left = new_curr.left
            else:
                new_curr = curr.right
                while new_curr.left:
                    new_curr = new_curr.left
                self.remove(new_curr.key)
                curr.key = new_curr.key
                curr.val = new_curr.val         

    def getInorderKeys(self) -> List[int]:
        vals = []
        if not self.root:
            return []
        
        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            vals.append(root.key)
            dfs(root.right)
        
        dfs(self.root)
        return vals
