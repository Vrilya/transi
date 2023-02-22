import tkinter as tk
from PIL import Image, ImageTk

# Skapa huvudfönstret
root = tk.Tk()
root.title("Mitt fönster")
root.geometry("1280x800")
root.resizable(False, False)

# Läs in bakgrundsbilden
bg_image = Image.open("flyg.jpg")
bg_image = bg_image.resize((1280, 800), resample=Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Lägg till bakgrundsbilden i huvudfönstret
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Skapa en funktion som ersätter en karaktär med en bild
def replace_char_with_image(event):
    char = event.char
    if char == "a":
        replace_image = Image.open("replace_char.png")
        replace_image = replace_image.resize((50, 50), resample=Image.LANCZOS)
        replace_photo = ImageTk.PhotoImage(replace_image)
        canvas.create_image(50, 50, image=replace_photo)

# Skapa ett textfält där användaren kan skriva in text
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
canvas.bind("<Key>", replace_char_with_image)
canvas.focus_set()

# Visa fönstret
root.mainloop()

