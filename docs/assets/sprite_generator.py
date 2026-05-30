import cv2
import numpy as np
from pathlib import Path

INPUT_FILE = "./generated_image3.png"     
OUTPUT_DIR = "./"
MIN_SPRITE_AREA = 5000  # Adjust if your sprites are smaller/larger
PADDING = 5            

def main():
    input_path = Path(INPUT_FILE)
    if not input_path.exists():
        print(f"Error: Could not find '{input_path}'.")
        return

    # Read the image and completely ignore any fake alpha channels
    img = cv2.imread(str(input_path), cv2.IMREAD_COLOR)
    if img is None:
        print("Error: Could not read image.")
        return

    # Convert to HSV color space to target the checkerboard
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Checkerboards are light gray and white.
    # In HSV: Saturation is near 0 (colorless), Value is high (bright).
    # This range targets everything from medium-light gray to pure white.
    lower_checkerboard = np.array([0, 0, 150])
    upper_checkerboard = np.array([180, 50, 255])
    
    # Find all pixels that match the fake checkerboard
    bg_mask = cv2.inRange(hsv, lower_checkerboard, upper_checkerboard)
    
    # Invert the mask: Sprites become WHITE (255), Background becomes BLACK (0)
    mask = cv2.bitwise_not(bg_mask)

    kernel = np.ones((7, 7), np.uint8)
    # Erase the tiny specks of noise left by the AI's imperfect checkerboard
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    # Fill in any accidental holes inside your actual sprite
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)

    # Find contours (RETR_EXTERNAL ensures we only get the outer boundary)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    outdir = Path(OUTPUT_DIR)
    outdir.mkdir(parents=True, exist_ok=True)
    
    count = 1
    bounding_boxes = [cv2.boundingRect(c) for c in contours]
    bounding_boxes.sort(key=lambda b: (b[1] // 50, b[0])) 

    for x, y, w, h in bounding_boxes:
        if w * h < MIN_SPRITE_AREA:
            continue

        x1 = max(0, x - PADDING)
        y1 = max(0, y - PADDING)
        x2 = min(img.shape[1], x + w + PADDING)
        y2 = min(img.shape[0], y + h + PADDING)

        sprite = img[y1:y2, x1:x2]

        output_path = outdir / f"sprite3_{count:02d}.png"
        cv2.imwrite(str(output_path), sprite)
        print(f"Saved: {output_path}")
        count += 1

    print(f"\nDone! Extracted {count - 1} sprites")

if __name__ == "__main__":
    main()