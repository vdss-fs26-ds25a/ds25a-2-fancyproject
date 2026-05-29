from PIL import Image
from collections import deque
from pathlib import Path
import math

# ---- CONFIG ----
INPUT_FILE = "/Users/jay/Documents/FS26/Vis & DS Storytelling/Semesterarbeit/assets/generated_image.png"     # change to your PNG filename
OUTPUT_DIR = "/Users/jay/Documents/FS26/Vis & DS Storytelling/Semesterarbeit/assets/"

COLS = 5
ROWS = 3

OUTER_MARGIN_X = 30   # left/right margin around whole sheet
OUTER_MARGIN_Y = 25   # top/bottom margin around whole sheet
GAP_X = 18            # horizontal gap between cells
GAP_Y = 22            # vertical gap between cells

TRIM = True           # trim transparent/white empty space inside each cell
PADDING = 6           # padding added after trim
WHITE_THRESHOLD = 245 # treat near-white as empty background

def is_empty_pixel(r, g, b, a):
    if a == 0:
        return True
    if r >= WHITE_THRESHOLD and g >= WHITE_THRESHOLD and b >= WHITE_THRESHOLD:
        return True
    return False

def trim_cell(cell):
    px = cell.load()
    w, h = cell.size

    min_x, min_y = w, h
    max_x, max_y = -1, -1

    for x in range(w):
        for y in range(h):
            r, g, b, a = px[x, y]
            if not is_empty_pixel(r, g, b, a):
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    if max_x == -1:
        return cell

    min_x = max(0, min_x - PADDING)
    min_y = max(0, min_y - PADDING)
    max_x = min(w, max_x + PADDING + 1)
    max_y = min(h, max_y + PADDING + 1)

    return cell.crop((min_x, min_y, max_x, max_y))

def main():
    img = Image.open(INPUT_FILE).convert("RGBA")
    w, h = img.size

    usable_w = w - 2 * OUTER_MARGIN_X - (COLS - 1) * GAP_X
    usable_h = h - 2 * OUTER_MARGIN_Y - (ROWS - 1) * GAP_Y

    cell_w = usable_w // COLS
    cell_h = usable_h // ROWS

    outdir = Path(OUTPUT_DIR)
    outdir.mkdir(parents=True, exist_ok=True)

    count = 1
    for row in range(ROWS):
        for col in range(COLS):
            x1 = OUTER_MARGIN_X + col * (cell_w + GAP_X)
            y1 = OUTER_MARGIN_Y + row * (cell_h + GAP_Y)
            x2 = x1 + cell_w
            y2 = y1 + cell_h

            cell = img.crop((x1, y1, x2, y2))

            if TRIM:
                cell = trim_cell(cell)

            cell.save(outdir / f"sprite_{count:02d}.png")
            count += 1

    print(f"Done. Exported {count - 1} PNG files to {outdir.resolve()}")

if __name__ == "__main__":
    main()
