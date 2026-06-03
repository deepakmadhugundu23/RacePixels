import sys, random, time, ctypes
import numpy as np
from PIL import Image
from colorama import init, Fore

init(autoreset=True)

image = Image.open("input.bmp").convert("RGB")
data = np.array(image)

def racepixels(grid):
    newgrid = grid.copy()
    rows, cols, _ = grid.shape
    
    white_pixels = np.argwhere((grid == [255, 255, 255]).all(axis=2))
    np.random.shuffle(white_pixels)
    
    for r, c in white_pixels:
        potential_neighbors = []
        if r > 0: potential_neighbors.append(grid[r-1, c])
        if r < rows-1: potential_neighbors.append(grid[r+1, c])
        if c > 0: potential_neighbors.append(grid[r, c-1])
        if c < cols-1: potential_neighbors.append(grid[r, c+1])
        
        for n in potential_neighbors:
            n = np.array(n)
            is_white = (n == [255, 255, 255]).all()
            is_wall = (n == [0, 0, 0]).all()
            
            if not is_white and not is_wall:
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

iteration = 0
while True:
    olddata = data.copy()
    data = racepixels(data)
    printgrid(data)
    
    if np.array_equal(data, olddata):
        finalimage = Image.fromarray(data)
        finalimage.save("output.bmp")
        print(f"out.bmp created after {iteration} iterations")
        break
    
    iteration += 1
    time.sleep(0.05)
