# My Answer
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
        return image
    else:
        original_color = image[sr][sc]
        image[sr][sc] = color
        if sr - 1 >= 0:
            if image[sr-1][sc] == original_color:
                self.floodFill(image, sr - 1, sc, color)
        if (sc + 1) < len(image[0]):
            if image[sr][sc+1] == original_color:
                self.floodFill(image, sr, sc + 1, color)
        if (sr + 1) < len(image):
            if image[sr+1][sc] == original_color:
                self.floodFill(image, sr + 1, sc, color)
        if sc - 1 >= 0:
            if image[sr][sc-1] == original_color:
                self.floodFill(image, sr , sc -1, color)
    return image   


# Optimal Answer
def floodFill(self, image, sr, sc, newColor):
    originalColor = image[sr][sc]
    if originalColor == newColor:
        return image
    
    def fill(r, c):
        # Check if the current pixel is within bounds and matches the original color
        if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == originalColor:
            image[r][c] = newColor
            # Recursively fill the adjacent pixels
            fill(r - 1, c)  # Up
            fill(r + 1, c)  # Down
            fill(r, c  - 1)  # Left
            fill(r, c + 1)  # Right
    
    fill(sr, sc)
    return image
