import sys, random, time, ctypes
import numpy as np
from PIL import Image
from colorama import init, Fore

init(autoreset=True)

image = Image.open("input.bmp").convert("RGB")
data = np.array(image)

def growpixels(grid):
    newgrid = grid.copy()
    rows, cols, _ = grid.shape
    coords = [(r, c) for r in range(1, rows-1) for c in range(1, cols-1)]
    random.shuffle(coords)
    for r, c in coords:
        if (grid[r, c] == [255, 255, 255]).all():
            neighbors = [grid[r-1, c], grid[r+1, c], grid[r, c-1], grid[r, c+1]]
            for n in neighbors:
                if not (n == [255, 255, 255]).all() and not (n == [0, 0, 0]).all():
                    newgrid[r, c] = n
                    break
    return newgrid

PIXEL = "█"

def printgrid(grid):
    sys.stdout.write("\033[H")
    for row in grid:
        line = ""
        for p in row:
            if (p == [255,0,0]).all(): line += Fore.RED + PIXEL
            elif (p == [0,0,255]).all(): line += Fore.BLUE + PIXEL
            elif (p == [0,0,0]).all(): line += "█"
            else: line += " "
        sys.stdout.write(line + "\n")
    sys.stdout.flush()

sys.stdout.write("\033[2J")

for _ in range(200):
    data = growpixels(data)
    printgrid(data)
    time.sleep(0.05)

data[(data == [255, 255, 255]).all(axis=2)] = [0, 0, 255]

Image.fromarray(data).save("output.bmp")
print("check output.bmp")
