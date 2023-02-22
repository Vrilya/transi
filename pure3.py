from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw

def get_replaced_image(image, character, replacement_image_path):
    # Open replacement image and convert to RGBA
    replacement_image = Image.open(replacement_image_path).convert("RGBA")
    # Create a new image with the same size as the input image
    replaced_image = Image.new("RGBA", image.size)
    # Iterate over every pixel in the input image
    for x in range(image.width):
        for y in range(image.height):
            # Get the current pixel value
            pixel = image.getpixel((x, y))
            # Check if the pixel matches the character we want to replace
            if chr(pixel[0]) == character:
                # If it does, replace the pixel with the corresponding pixel in the replacement image
                replaced_image.putpixel((x, y), replacement_image.getpixel((x % replacement_image.width, y % replacement_image.height)))
            else:
                # If it doesn't, keep the original pixel value
                replaced_image.putpixel((x, y), pixel)
    return replaced_image

# Create the root window
root = Tk()
root.title("Transi")
root.geometry("1280x800")
root.resizable(False, False)

# Load the background image
image = Image.open("flyg.jpg")
image = image.resize((1280, 800), resample=Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)

# Replace a character with an image
image = get_replaced_image(image, "a", "replace_char.png")
text_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
image_font = ImageFont.truetype("arial.ttf", 14)
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel leo elit. Maecenas ac mi blandit, elementum tellus id, fringilla felis. Etiam tempor nibh urna, sit amet lobortis nisi facilisis et. Donec vitae elementum velit, nec efficitur urna. Vivamus consectetur sapien ac est molestie iaculis. Vivamus eget ante vitae ex lacinia bibendum. Donec vel pharetra urna. Suspendisse vitae nunc in eros posuere semper a sit amet augue. Quisque sodales odio sit amet mi euismod, vel finibus est molestie. Fusce id erat at urna accumsan euismod eget quis odio. Donec mollis fermentum nunc. Aliquam eu faucibus lorem. Etiam interdum tortor eget eleifend elementum. Aliquam erat volutpat."
text_x = 50
text_y = 50
for char in text:
    if char == " ":
        text_x += image_font.getsize(char)[0]
    else:
        char_image = Image.new("RGBA", image_font.getsize(char), (0, 0, 0, 0))

