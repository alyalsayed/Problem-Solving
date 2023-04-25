class Solution(object):
    def floodFill(self, image, sr, sc, color):
        # Get the original color of the seed pixel
        original_color = image[sr][sc]
        
        # If the seed pixel is already the fill color, return image
        if original_color == color:
            return image
        
        # Recursively fill the region starting from the seed pixel
        self.fill(image, sr, sc, original_color, color)
        
        return image
    
    def fill(self, image, x, y, original_color, fill_color):
        # If the pixel is outside the image boundary or doesn't match the original color, return
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != original_color:
            return
        
        # Set the color of the current pixel to the fill color
        image[x][y] = fill_color
        
        # Recursively fill the adjacent pixels
        self.fill(image, x+1, y, original_color, fill_color) # right
        self.fill(image, x-1, y, original_color, fill_color) # left
        self.fill(image, x, y+1, original_color, fill_color) # up
        self.fill(image, x, y-1, original_color, fill_color) # down