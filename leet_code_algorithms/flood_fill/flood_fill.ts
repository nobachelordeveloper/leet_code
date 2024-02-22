/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
const floodFill = (
  image: number[][],
  sr: number,
  sc: number,
  color: number
): number[][] => {
  let originalColor = image[sr][sc];
  if (originalColor === color) {
    return image;
  }
  const fill = (r, c) => {
    if (0 <= r && r < image.length && 0 <= c && c < image[0].length) {
      if (image[r][c] === originalColor) {
        image[r][c] = color;
        fill(r - 1, c);
        fill(r + 1, c);
        fill(r, c - 1);
        fill(r, c + 1);
      }
    }
  };
  fill(sr, sc);
  return image;
};

//Set up RETURNS for invalid conditions
const floodFillOptimal = (
  image: number[][],
  sr: number,
  sc: number,
  color: number
): number[][] => {
  const targetColor = image[sr][sc];
  if (targetColor === color) return image;
  const X = image.length - 1,
    Y = image[0].length - 1;
  const dfs = (x, y) => {
    if (x < 0 || x > X || y < 0 || y > Y) return;
    if (image[x][y] !== targetColor) return;
    image[x][y] = color;
    dfs(x - 1, y);
    dfs(x + 1, y);
    dfs(x, y - 1);
    dfs(x, y + 1);
  };
  dfs(sr, sc);
  return image;
};
