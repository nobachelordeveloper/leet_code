#My Brute Force Solution
def lowestCommonAncestor(
    self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":
    def checkNode(node):
        history = []
        pHistory = []
        qHistory = []

        def searchNode(history, node, target):
            if node != None:
                new_history = history + [node]
                if node.val == target.val:
                    return new_history
                else:
                    left_search = searchNode(new_history, node.left, target)
                    if left_search != None:
                        return left_search
                    right_search = searchNode(new_history, node.right, target)
                    if right_search != None:
                        return right_search
                    return None

        pHistory = searchNode(history, node, p)
        qHistory = searchNode(history, node, q)
        if pHistory != None and qHistory != None:
            return True
        else:
            return False

    if checkNode(root):
        current = root
    left = checkNode(root.left)
    right = checkNode(root.right)
    while (left == True or right == True) and current != None:
        left = checkNode(current.left)
        right = checkNode(current.right)
        if left:
            current = current.left
        if right:
            current = current.right
    if current:
        return current


#Best Solution
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    else:
        return root

'''
Characteristics of a Binary Search Tree:

Node Structure: Each node in a BST contains a key (or value), and pointers to its left and right children. The key is a data item that the tree organizes (e.g., numbers, strings, etc.).

Ordered Structure: For every node, all elements in the left subtree are less than the node's key, and all elements in the right subtree are greater than the node's key. This property must be true for all nodes in the tree.

No Duplicate Nodes: Each node must have a unique key. However, the specific handling of duplicates can vary based on the implementation or application requirements.
'''