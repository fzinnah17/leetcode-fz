"""
Bucket Filling
There is often a "bucket fill" tool in digital graphics tools that only paints cells that are next to each other. In one fill, a modified bucket tool changes the color of adjacent cells with the same color that are linked horizontally or vertically but not diagonally. Find the fewest number of fills needed to completely re-paint a picture shown as a 2-D array of letters representing colors.

["aabba", "aabba", "aaacb"] as an example 5 is the output. 

Each string is a row of the image, and each letter is the color of a cell. The diagram below shows the five fills that are needed to repaint the image. It takes two fills for a and b, and just one fill for c.

Description of the Function:
Complete the required function strokes.
strokesRequired is made of the following parameters):
picture[h] is an array of strings, each of which represents a row of the picture to be painted.
Output: int: the number of fills needed to repaint the image.
"""

def strokesRequired(picture):
    def fill(x, y, color):
        if x < 0 or y < 0 or x >= len(picture) or y >= len(picture[0]) or picture[x][y] != color:
            return
        picture[x][y] = '#'
        fill(x + 1, y, color)  # fill adjacent cells
        fill(x - 1, y, color)
        fill(x, y + 1, color)
        fill(x, y - 1, color)

    fills = 0
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] != '#':
                fills += 1
                fill(i, j, picture[i][j])

    return fills
