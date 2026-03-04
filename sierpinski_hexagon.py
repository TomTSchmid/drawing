from PIL import Image
import numpy as np
import math
import random

img_w, img_h = 10_000, 10_000
data = np.zeros((img_h, img_w, 3), dtype=np.uint8)

# Center of the image
center_x, center_y = img_w / 2, img_h / 2

# Size of each triangle (distance from center to base)
# size = 9_950
size = 10_000
offset = 12
iterations = 10_000_000

# 6 different colors: red, green, blue, yellow, magenta, cyan
colors = [
    [255, 0, 0],    # red
    # [255, 165, 0],  # orange
    [165, 165, 0],  # yellow
    [0, 200, 0],    # green
    [0, 165, 165],  # cyan
    [0, 0, 165],    # blue
    [165, 0, 165],  # magenta
]

# Create 6 triangles arranged in a hexagon, each pointing to the center
triangles = []
for i in range(6):
    # Top vertex (pointing to center)
    top_x = center_x + math.cos(math.radians(i * 60 + 30)) * offset
    top_y = center_y + math.sin(math.radians(i * 60 + 30)) * offset

    # Base left vertex (away from center)
    base_left_x = top_x + math.cos(math.radians(i * 60)) * (size)
    base_left_y = top_y + math.sin(math.radians(i * 60)) * (size)

    # Base right vertex (away from center)
    base_right_x = top_x + math.cos(math.radians((i + 1) * 60)) * (size)
    base_right_y = top_y + math.sin(math.radians((i + 1) * 60)) * (size)

    triangle = [
        [top_x, top_y],
        [base_left_x, base_left_y],
        [base_right_x, base_right_y],
    ]
    triangles.append(triangle)

# Generate each Sierpinski triangle using the chaos game
for triangle_idx, triangle in enumerate(triangles):
    color = colors[triangle_idx]

    # Start at one of the vertices
    pos = triangle[0][:]

    for i in range(iterations):
        # Pick a random vertex
        r = random.randint(0, 2)

        # Move halfway to that vertex
        x = round((pos[0] + triangle[r][0]) / 2)
        y = round((pos[1] + triangle[r][1]) / 2)

        # Color the pixel if it's within bounds
        if 0 <= y < img_h and 0 <= x < img_w:
            data[y, x] = color

        pos = [x, y]

screen_w, screen_h = 3840, 1600

output_data = data[
    int(center_y - screen_h // 2) : int(center_y + screen_h // 2),
    int(center_x - screen_w // 2) : int(center_x + screen_w // 2),
]

img = Image.fromarray(output_data, "RGB")
# img = Image.fromarray(data, "RGB")
img.save("sierpinski_hexagon_3.png")
print("Saved sierpinski_hexagon_3.png")
