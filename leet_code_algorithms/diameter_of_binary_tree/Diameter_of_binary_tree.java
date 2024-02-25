package diameter_of_binary_tree;

public class Diameter_of_binary_tree {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    private int max_depth;

    public int diameterOfBinaryTree(TreeNode root) {
        this.max_depth = 0;
        getMaxDepth(root);
        return this.max_depth;
    }

    public int getMaxDepth(TreeNode node) {
        if (node == null) {
            return -1;
        }
        int left = getMaxDepth(node.left);
        int right = getMaxDepth(node.right);
        this.max_depth = Math.max(left + right + 2, this.max_depth);
        return 1 + Math.max(left, right);
    }
}
