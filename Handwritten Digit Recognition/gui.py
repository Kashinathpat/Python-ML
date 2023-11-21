import tkinter as tk

import PIL
from PIL import Image, ImageDraw, ImageGrab
import use_model


def start_drawing(event):
    global drawing
    drawing = True
    draw(event)


def draw(event):
    if drawing:
        row = event.y // pixel_size
        col = event.x // pixel_size
        pixel_x = col * pixel_size
        pixel_y = row * pixel_size
        canvas.create_rectangle(pixel_x, pixel_y, pixel_x + pixel_size, pixel_y + pixel_size, fill="black")


def stop_drawing(event):
    global drawing
    drawing = False


def submit_drawing():
    x = root.winfo_x() + canvas.winfo_x() + 22
    y = root.winfo_y() + canvas.winfo_y() + 22
    image = PIL.ImageGrab.grab(bbox=(x, y, x + canvas_size, y + canvas_size))
    image = image.resize((28, 28))
    image.save("canvas.png")
    prediction_label.config(text=f"Number is : {use_model.predict_image('canvas.png')}")

def clear_canvas():
    canvas.delete("all")

# Set canvas size and pixel size
canvas_size = 500
pixel_size = 20

# Create a larger window
root = tk.Tk()
root.title("Drawing App")
root.geometry(f"{canvas_size + 50}x{canvas_size + 70}")

# Create canvas
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white", cursor="cross")
canvas.pack()

# Initialize drawing settings
drawing = False

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_drawing)
submit_button.pack()

# Create clear button
clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack()
# Create clear button
prediction_label = tk.Label(root, text="Number is : ")
prediction_label.pack()

# Bind mouse events
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.mainloop()
