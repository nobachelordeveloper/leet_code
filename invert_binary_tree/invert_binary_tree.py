# My Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def invertNode(node: Optional[TreeNode]):
        current = node
        if current == None:
            return
        leftPlaceholder = current.left if current.left else None
        current.left = node.right if node.right else None
        current.right = leftPlaceholder
        invertNode(current.left)
        invertNode(current.right)
    if root == None:
        return root
    else:
        invertNode(root)
    return root

# Optimal solution
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    self.invertTree(root.left)
    self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root
