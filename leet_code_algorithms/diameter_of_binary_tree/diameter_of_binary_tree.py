class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.max_depth = 0

    def dfs(root):
        if not root:
            return - 1
        left = dfs(root.left)
        right = dfs(root.right)
        self.max_depth = max(self.max_depth, left + right + 2)
        return 1 + max(left, right)
    dfs(root)
    return self.max_depth

# WITHOUT USING OOP AND SELF
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # use list for a mutable object that could be used for a variable with globals cope
    res = [0]

    def dfs(root):
        if not root:
            return - 1
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], left + right + 2)
        return 1 + max(left, right)
    dfs(root)
    return res[0]
