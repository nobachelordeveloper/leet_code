package invert_binary_tree;

public class Invert_binary_tree {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public TreeNode invertTree(TreeNode root) {
        if(root == null) {
            return root;
        }
        TreeNode leftPlaceholder = root.left;
        root.left = root.right;
        root.right = leftPlaceholder;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}