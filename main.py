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
        current = grid[r, c]
        if (current == [0, 0, 0]).all(): continue
        
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        nr, nc = random.choice(neighbors)
        neighbor = grid[nr, nc]
        
        if not (neighbor == [0, 0, 0]).all() and not (neighbor == current).all():
            if random.random() < 0.1:
                newgrid[nr, nc] = current
                
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

for _ in range(500):
    data = growpixels(data)
    printgrid(data)
    time.sleep(0.01)

Image.fromarray(data).save("output.bmp")
print("check output.bmp")
