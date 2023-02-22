from tkinter import *
from PIL import ImageTk


root = Tk()

# Sätt standardstorleken på fönstret till 1200x800
root.geometry("1200x800")

# Förhindra användaren från att ändra storleken på fönstret
root.resizable(width=False, height=False)

canvas = Canvas(root, width=1200, height=800, bg='blue')
canvas.pack(expand=YES, fill=BOTH)

# Lägg till en bakgrundsbild
bg_image = ImageTk.PhotoImage(file="C:/test/flyg.jpg")
canvas.create_image(0, 0, image=bg_image, anchor=NW)

input_text = StringVar()
input_entry = Entry(canvas, textvariable=input_text)
input_entry.pack(side=TOP, padx=10, pady=10)

# Skapa en ImageFont för bokstaven "Ö" som innehåller en bild
image_font = ImageFont.load_default()
image = Image.open("C:/test/replace_char.png")
image = image.resize((image_font.getsize("Ö")), Image.ANTIALIAS)
image_font = ImageFont.truetype("arial.ttf", 14)
image_font.font.getmask("Ö")
image_font.font.paste(im=image, box=(0, 0), mask=image.split()[3])

# Skapa text med tecken som ska bytas ut med bilden
text = "Hej Ö"
text_x = 128
text_y = 256

# Loopa genom varje tecken i texten och skapa texten med tecken som ska bytas ut
for char in text:
    if char == "Ö":
        canvas.create_text(text_x, text_y, text=char, fill="white", font=image_font)
        text_x += image_font.getsize(char)[0]
    else:
        canvas.create_text(text_x, text_y, text=char, fill="white", font=("Arial", 14))
        text_x += canvas.textwidth(char, font=("Arial", 14))

# Lägg till en bild
image = ImageTk.PhotoImage(file="C:/test/kuru.png")
canvas.create_image(128, 128, image=image, anchor=NW)

root.mainloop()