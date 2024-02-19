# My Answer
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return [True, 0]
        left, right = dfs(node.left), dfs(node.right)
        if left[0] and right[0] and abs(left[1] - right[1] <= 1):
            return [True, 1 + max(left[1], right[1])]
        else:
            return [False]
    return dfs(root)[0]
