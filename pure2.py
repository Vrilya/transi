from tkinter import *
from PIL import Image, ImageFont, ImageTk

root = Tk()
root.geometry("1280x800")
root.resizable(False, False)
root.title("Transi")

image = Image.open("flyg.jpg")
image = image.resize((1280, 800), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)

canvas = Canvas(root, width=1280, height=800)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=background_image)

replace_char = Image.open("replace_char.png")
replace_char = replace_char.resize((20, 20), Image.LANCZOS)
replace_char = ImageTk.PhotoImage(replace_char)

def on_key_press(event):
    if event.char == "a":
        canvas.create_image(100, 100, anchor=NW, image=replace_char)
    else:
        text_x, text_y = 0, 0
        for char in event.char:
            text_image = Image.new("RGBA", image_font.getsize(char), (0, 0, 0, 0))
            text_draw = ImageDraw.Draw(text_image)
            text_draw.text((0, 0), char, font=image_font, fill="white")
            text_photo = ImageTk.PhotoImage(text_image)
            canvas.create_image(text_x, text_y, anchor=NW, image=text_photo)
            text_x += text_photo.width()
            text_y += text_photo.height()

image_font = ImageFont.truetype("arial.ttf", 14)
canvas.bind("<Key>", on_key_press)
canvas.focus_set()
root.mainloop()

