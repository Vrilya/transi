from tkinter import *
from PIL import ImageTk

def get_input_text():
    text = input_text.get()
    print("Input text: ", text)

canvas = Canvas(width = 1000, height = 600, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)

input_text = StringVar()
input_entry = Entry(canvas, textvariable=input_text)
input_entry.pack(side=TOP, padx=10, pady=10)

image = ImageTk.PhotoImage(file = "C:/test/kuru.png")
canvas.create_image(128, 128, image = image, anchor = NW)

button = Button(canvas, text="Get input text", command=get_input_text)
button.pack(side=TOP, padx=10, pady=10)

mainloop()