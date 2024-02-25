export {};

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
const diameterOfBinaryTree = (root: TreeNode | null) => {
  let maxDepth = 0;
  const dfs = (node: TreeNode | null) => {
    if (!node) {
      return -1;
    }
    const left = dfs(node.left);
    const right = dfs(node.right);
    maxDepth = Math.max(left + right + 2, maxDepth);
    return 1 + Math.max(left, right);
  };
  dfs(root);
  return maxDepth;
};
