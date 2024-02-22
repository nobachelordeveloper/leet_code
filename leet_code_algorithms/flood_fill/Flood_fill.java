package flood_fill;

public class Flood_fill {
    private int[][] image;
    private int originalColor;
    private int color;

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        this.image = image;
        this.originalColor = image[sr][sc];
        this.color = color;
        if (originalColor == color) {
            return image;
        }
        int X = image.length - 1;
        int Y = image[0].length - 1;
        fill(sr, sc, X, Y);
        return image;
    }

    public void fill(int x, int y, int X, int Y) {
        if (x < 0 || x > X || y < 0 || y > Y) {
            return;
        }
        if (this.image[x][y] != originalColor) {
            return;
        }
        this.image[x][y] = color;
        fill(x - 1, y, X, Y);
        fill(x + 1, y, X, Y);
        fill(x, y - 1, X, Y);
        fill(x, y + 1, X, Y);
    }
}
