from PIL import Image, ImageDraw

# Define dimensions for the clipboard image
image_sizes = [(128, 128), (48, 48), (16, 16)]

# Iterate over each size
for size in image_sizes:
    # Create a new image with a white background
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Draw clipboard shape
    clip_color = (200, 200, 200)
    clipboard_color = (181, 101, 29)

    draw.rounded_rectangle([(size[0]//4, size[1]//8), (size[0]//4 * 3, size[1]//8 * 7)], fill=clipboard_color, radius=size[1] // 7)

    # Draw top part of clipboard
    draw.polygon([(size[0]//4, size[1]//8), (size[0]//4 * 3, size[1]//8), (size[0]//4 * 3, size[1]//8 * 2), (size[0]//4, size[1]//8 * 2)], fill=clip_color)

    # Save the image with corresponding filename
    filename = f"icon-{size[0]}.png"
    image.save(filename)
