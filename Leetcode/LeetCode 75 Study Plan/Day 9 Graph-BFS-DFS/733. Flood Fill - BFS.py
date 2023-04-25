class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        
        target_color = image[sr][sc]
        
        # If the starting pixel already has the new color, return the image
        if target_color == newColor:
            return image
        
        # Initialize a queue with the starting pixel
        queue = [(sr, sc)]
        
        while queue:
            row, col = queue.pop(0)
            
            # Check if the current cell is within the image and has the target color
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != target_color:
                continue
            
            # Change the color of the current cell to the new color
            image[row][col] = newColor
            
            # Add the adjacent cells to the queue
            queue.append((row+1, col))
            queue.append((row-1, col))
            queue.append((row, col+1))
            queue.append((row, col-1))
        
        # Return the modified image
        return image