package balanced_binary_tree;

public class balanced_binary_tree {
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

    public boolean isBalanced(TreeNode root) {
        return dfs(root).found;
    }

    public DfsResult dfs(TreeNode node) {
        if (node == null) {
            return new DfsResult(true, 0);
        }
        DfsResult left = dfs(node.left);
        DfsResult right = dfs(node.right);
        if (left.found && right.found && Math.abs(left.value - right.value) <= 1) {
            return new DfsResult(true, 1 + Math.max(left.value, right.value));
        } else {
            return new DfsResult(false, 0);
        }
    }

    public class DfsResult {
        public boolean found;
        public int value;

        public DfsResult(boolean found, int value) {
            this.found = found;
            this.value = value;
        }
    }
}
