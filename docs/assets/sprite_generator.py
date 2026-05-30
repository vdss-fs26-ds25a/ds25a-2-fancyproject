import cv2
import numpy as np
from pathlib import Path

# ---- CONFIG ----
INPUT_FILE = "./generated_image2.png"     
OUTPUT_DIR = "./"
MIN_SPRITE_AREA = 500  # Ignore tiny artifacts/noise smaller than this many pixels
PADDING = 5            # Pixels of padding to add around the cropped sprite

def main():
    input_path = Path(INPUT_FILE)
    if not input_path.exists():
        print(f"Error: Could not find '{input_path}'.")
        return

    # 1. Load the image with Alpha channel (Transparency)
    img = cv2.imread(str(input_path), cv2.IMREAD_UNCHANGED)
    if img is None:
        print("Error: Could not read image.")
        return

    # 2. Create a mask of the visible pixels
    # If the image has an alpha channel (transparent background)
    if img.shape[2] == 4:
        alpha_channel = img[:, :, 3]
        _, mask = cv2.threshold(alpha_channel, 10, 255, cv2.THRESH_BINARY)
    else:
        # If the image has a white/solid background, we look for non-white pixels
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # 3. Find contours (the outlines of the sprites)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    outdir = Path(OUTPUT_DIR)
    outdir.mkdir(parents=True, exist_ok=True)
    
    count = 1
    
    # Sort contours from top-left to bottom-right to keep them somewhat in order
    bounding_boxes = [cv2.boundingRect(c) for c in contours]
    # Sort primarily by Y (rows), then by X (columns)
    bounding_boxes.sort(key=lambda b: (b[1] // 50, b[0])) 

    for x, y, w, h in bounding_boxes:
        # Ignore tiny specks or noise
        if w * h < MIN_SPRITE_AREA:
            continue

        # Add padding but ensure we don't go outside the image boundaries
        x1 = max(0, x - PADDING)
        y1 = max(0, y - PADDING)
        x2 = min(img.shape[1], x + w + PADDING)
        y2 = min(img.shape[0], y + h + PADDING)

        # Crop the sprite
        sprite = img[y1:y2, x1:x2]

        # Save it
        output_path = outdir / f"sprite2_{count:02d}.png"
        cv2.imwrite(str(output_path), sprite)
        print(f"Saved: {output_path}")
        count += 1

    print(f"\nDone! Successfully extracted {count - 1} individual sprites.")

if __name__ == "__main__":
    main()