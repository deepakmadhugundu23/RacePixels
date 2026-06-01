import random
import numpy as np
from PIL import Image

image = Image.open("input.bmp").convert("RGB")
data = np.array(image)

def racepixels(grid):
    newgrid = grid.copy()
    rows, cols, channels = grid.shape

    coords = [(r, c) for r in range(1, rows-1) for c in range(1, cols-1)]
    random.shuffle(coords)

    for r, c in coords:
        if np.all(grid[r, c] == [255, 255, 255]):
            coordinates = [grid[r-1, c], grid[r+1, c], grid[r, c-1], grid[r, c+1]]
            for n in coordinates:
                if not np.all(n == [255, 255, 255]) and not np.all(n == [0, 0, 0]):
                    newgrid[r, c] = n
                    break
    return newgrid 

for _ in range(200):
    data = racepixels(data)

resultimage = Image.fromarray(data)
resultimage.save("output.bmp")
print("check output.bmp")
