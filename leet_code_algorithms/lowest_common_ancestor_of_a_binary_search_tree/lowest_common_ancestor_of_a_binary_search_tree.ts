// Definition for a binary tree node.
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

const lowestCommonAncestor = (
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null => {
  if (p!.val! < root!.val && q!.val < root!.val) {
    return lowestCommonAncestor(root!.left, p, q);
  } else if (p!.val > root!.val && q!.val > root!.val) {
    return lowestCommonAncestor(root!.right, p, q);
  } else {
    return root;
  }
};

//this keeps running until return condition is met
function lowestCommonAncestorOptimal(root, p, q) {
  while (root) {
    if (p.val > root.val && q.val > root.val) {
      root = root.right;
    } else if (p.val < root.val && q.val < root.val) {
      root = root.left;
    } else {
      return root;
    }
  }
}
