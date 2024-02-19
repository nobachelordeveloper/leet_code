// class TreeNode {
//   val: number;
//   left: TreeNode | null;
//   right: TreeNode | null;
//   constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//     this.val = val === undefined ? 0 : val;
//     this.left = left === undefined ? null : left;
//     this.right = right === undefined ? null : right;
//   }
// }

const isBalanced = (root: TreeNode) => {
  const dfs = (node: TreeNode | null) => {
    if (!node) {
      return [true, 0];
    }
    const left = dfs(node.left);
    const right = dfs(node.right);
    if (left[0] && right[0] && Math.abs(left[1] - right[1]) <= 1) {
      return [true, 1 + Math.max(left[1], right[1])];
    } else {
      return [false];
    }
  };
  return dfs(root)[0];
};
