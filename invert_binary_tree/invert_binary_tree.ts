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

const invertTree = (root: TreeNode | null): TreeNode | null => {
  if (!root) {
    return root;
  }
  const leftPlaceholder = root.left;
  root.left = root.right;
  root.right = leftPlaceholder;
  invertTree(root.left);
  invertTree(root.right);
  return root;
};
