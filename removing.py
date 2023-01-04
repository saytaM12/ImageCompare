import os
import tkinter
import math
from pynput import keyboard
from PIL import Image, ImageTk

directory: str = 'mnt/c/Users/matya/Desktop/home/culture'
new_width: int = 600
left: bool = False
right: bool = False

def on_press(key):
    if key == keyboard.Key.left:
        global left
        left = True
        return False
    elif key == keyboard.Key.right:
        global right
        right = True
        return False
    return False

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("image")
    root.geometry("+250+100")

    with open("pairs", "r") as f:
        file_text = f.read()
        pairs = file_text.split(';')

    for pair in pairs:
        files = pair.split(',')
        file1 = files[0]
        file2 = files[1]
        img1 = Image.open(os.path.join(directory, file1))
        img2 = Image.open(os.path.join(directory, file2))
        aspect_ratio1 = img1.width/img1.height
        while (new_width/aspect_ratio1 > 800):
            new_width -= 50
        resize_image1 = img1.resize(
            (new_width, math.ceil(new_width/aspect_ratio1)))
        i1 = ImageTk.PhotoImage(resize_image1)
        my_image_label = tkinter.Label(image=i1).grid(row=1, column=0)
        name1_label = tkinter.Label(text=f"{file1[-10::]}").grid(row=2, column=0)
        resolution1_label = tkinter.Label(
            text=f"{img1.width}, {img1.height}").grid(row=3, column=0)

        aspect_ratio2 = img2.width/img2.height
        while (new_width/aspect_ratio2 > 800):
            new_width -= 50
        resize_image2 = img2.resize(
            (new_width, math.ceil(new_width/aspect_ratio2)))
        i2 = ImageTk.PhotoImage(resize_image2)
        my_image_label = tkinter.Label(image=i2).grid(row=1, column=1)
        name2_label = tkinter.Label(text=f"{file2[-10::]}").grid(row=2, column=1)
        resolution2_label = tkinter.Label(
            text=f"{img2.width}, {img2.height}").grid(row=3, column=1)

        root.update_idletasks()
        root.update()

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

            if left or right:
                os.remove(os.path.join(directory, (file1 if left else file2)))

        left = right = False